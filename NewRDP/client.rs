use std::io::Read;
use std::net::TcpStream;
use winit::event_loop::{ControlFlow, EventLoop};
use winit::window::WindowBuilder;
use pixels::{Pixels, SurfaceTexture};

fn main() {
    // Conecta ao servidor
    let mut stream = TcpStream::connect("127.0.0.1:5000").expect("Falha ao conectar ao servidor.");

    // Cria uma janela para exibir os frames
    let event_loop = EventLoop::new();
    let window = WindowBuilder::new()
        .with_title("Streaming Gráfico")
        .build(&event_loop)
        .unwrap();

    // Configura o buffer de pixels
    let window_size = window.inner_size();
    let surface_texture = SurfaceTexture::new(window_size.width, window_size.height, &window);
    let mut pixels = Pixels::new(window_size.width, window_size.height, surface_texture)
        .expect("Falha ao criar o buffer de pixels.");

    // Loop principal
    event_loop.run(move |event, _, control_flow| {
        *control_flow = ControlFlow::Poll;

        match event {
            winit::event::Event::MainEventsCleared => {
                // Recebe o frame do servidor
                let mut frame = vec![0; pixels.frame().len()];
                stream.read_exact(&mut frame).expect("Falha ao receber o frame.");

                // Copia o frame para o buffer de pixels
                pixels.frame_mut().copy_from_slice(&frame);

                // Renderiza o frame na janela
                pixels.render().expect("Falha ao renderizar o frame.");
            }
            _ => (),
        }
    });
}