use scrap::{Capturer, Display};
use std::io::Write;
use std::net::TcpStream;
use std::time::Duration;

fn main() {
    // Captura a tela
    let display = Display::primary().expect("Não foi possível encontrar o display primário.");
    let mut capturer = Capturer::new(display).expect("Não foi possível iniciar a captura de tela.");

    // Conecta ao cliente
    let mut stream = TcpStream::connect("127.0.0.1:5000").expect("Falha ao conectar ao cliente.");

    loop {
        // Captura um frame
        let frame = capturer.frame().expect("Falha ao capturar o frame.");

        // Envia o frame para o cliente
        stream.write_all(&frame).expect("Falha ao enviar o frame.");

        // Espera um pouco antes de capturar o próximo frame
        std::thread::sleep(Duration::from_millis(1000 / 30)); // 30 FPS
    }
}

