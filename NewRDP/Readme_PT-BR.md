Aqui está um **exemplo passo a passo** de como executar o código Rust que capturei e transmiti frames de tela entre servidor e cliente. Vamos configurar e testar o projeto.

---

### **Passo 1: Configuração do Ambiente**
#### Pré-requisitos:
1. **Rust instalado** (use [rustup.rs](https://rustup.rs/) se não tiver).
2. **Bibliotecas de desenvolvimento gráfico** (no Linux, instale `libx11-dev` e `libwayland-dev`).
3. **FFmpeg** (opcional, para compressão avançada).

---

### **Passo 2: Criar o Projeto**
Abra um terminal e execute:
```bash
# Criar diretório para o projeto
mkdir rust_screen_stream
cd rust_screen_stream

# Iniciar um novo projeto Rust para o servidor
cargo new server
cd server
```

---

### **Passo 3: Adicionar Dependências**
Edite o arquivo `server/Cargo.toml` e adicione:
```toml
[package]
name = "server"
version = "0.1.0"
edition = "2021"

[dependencies]
scrap = "0.5"   # Para captura de tela
tokio = { version = "1.0", features = ["full"] }  # Para rede assíncrona
```

Repita o processo para o cliente:
```bash
cd ..
cargo new client
cd client
```

Edite `client/Cargo.toml`:
```toml
[package]
name = "client"
version = "0.1.0"
edition = "2021"

[dependencies]
winit = "0.28"  # Para criar janelas
pixels = "0.13" # Para renderização gráfica
tokio = { version = "1.0", features = ["full"] }
```

---

### **Passo 4: Implementar o Servidor**
Substitua o conteúdo de `server/src/main.rs` por:
```rust
use scrap::{Capturer, Display};
use std::io::Error;
use tokio::net::TcpListener;
use tokio::io::AsyncWriteExt;

#[tokio::main]
async fn main() -> Result<(), Error> {
    let display = Display::primary()?;
    let mut capturer = Capturer::new(display)?;
    let listener = TcpListener::bind("127.0.0.1:5000").await?;

    println!("Servidor aguardando conexões...");
    let (mut socket, _) = listener.accept().await?;

    loop {
        let frame = capturer.frame()?;
        socket.write_all(&frame).await?;
    }
}
```

---

### **Passo 5: Implementar o Cliente**
Substitua o conteúdo de `client/src/main.rs` por:
```rust
use pixels::{Pixels, SurfaceTexture};
use winit::event_loop::EventLoop;
use winit::window::WindowBuilder;
use tokio::net::TcpStream;
use tokio::io::AsyncReadExt;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut stream = TcpStream::connect("127.0.0.1:5000").await?;
    let event_loop = EventLoop::new();
    let window = WindowBuilder::new()
        .with_title("Streaming de Tela Rust")
        .build(&event_loop)?;

    let window_size = window.inner_size();
    let surface_texture = SurfaceTexture::new(window_size.width, window_size.height, &window);
    let mut pixels = Pixels::new(window_size.width, window_size.height, surface_texture)?;

    event_loop.run(move |event, _, control_flow| {
        control_flow.set_poll();

        match event {
            winit::event::Event::MainEventsCleared => {
                let frame = pixels.frame_mut();
                let mut buf = vec![0; frame.len()];

                // Bloqueia para simular recebimento assíncrono (em produção, use tokio::runtime)
                tokio::runtime::Runtime::new().unwrap().block_on(async {
                    stream.read_exact(&mut buf).await.unwrap();
                });

                frame.copy_from_slice(&buf);
                pixels.render().unwrap();
            }
            _ => (),
        }
    });
}
```

---

### **Passo 6: Executar o Projeto**
Abra **dois terminais**:

#### Terminal 1 (Servidor):
```bash
cd server
cargo run --release
```

#### Terminal 2 (Cliente):
```bash
cd client
cargo run --release
```

---

### **Passo 7: Resultado Esperado**
1. O **servidor** começará a capturar a tela e enviar frames para o cliente.
2. O **cliente** abrirá uma janela exibindo a tela do servidor em tempo real (aproximadamente 30 FPS).

---

### **Otimizações Recomendadas**
1. **Compressão de Vídeo**:
   - Adicione `ffmpeg-next` ao servidor para comprimir frames antes do envio.
   ```rust
   // Exemplo de compressão com FFmpeg (adicione ao servidor)
   use ffmpeg_next::format::context::Output;
   ```

2. **Aceleração por GPU**:
   - No cliente, substitua `pixels` por `wgpu` para renderização mais eficiente.

3. **Protocolo UDP**:
   - Troque `TcpStream` por `UdpSocket` para reduzir latência:
   ```rust
   use tokio::net::UdpSocket;
   ```

4. **Controle de FPS**:
   - Use `std::time::Duration` para ajustar a taxa de frames:
   ```rust
   std::thread::sleep(Duration::from_millis(1000 / 60)); // 60 FPS
   ```

---

### **Problemas Comuns e Soluções**
| Problema | Solução |
|----------|---------|
| Erro ao capturar tela no Linux | Instale `libx11-dev`: `sudo apt install libx11-dev` |
| Janela do cliente não responde | Use `control_flow.set_wait()` em vez de `set_poll()` |
| Frames lentos | Reduza a resolução ou ative compressão |

---

Este exemplo demonstra o fluxo básico. Para um sistema completo, você precisará implementar tratamento de erros, compressão e sincronização avançada. Rust oferece performance próxima ao C/C++, mas com segurança de memória garantida!