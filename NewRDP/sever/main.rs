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