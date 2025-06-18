use pixels::{Pixels, SurfaceTexture};
use winit::event_loop::EventLoop;
use winit::window::WindowBuilder;
use tokio::net::TcpStream;
use tokio::io::AsyncReadExt;

#[tokio::main]

async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut stream = TcpStream::connect("127.0.0.1:5000").await?; // Solicita conexao no cliente
    let event_loop = EventLoop::new(); 
    let window = WindowBuilder::new(); // cria a tela 
        .with_title("Streaming de Tela Rust") // nomeia Tela
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
