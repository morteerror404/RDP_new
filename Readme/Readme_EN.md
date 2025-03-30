# **Remote Screen Streaming with Rust (Server + Client Example)**

This guide demonstrates how to build a **basic screen streaming system** in Rust, where a **server captures the screen** and sends frames to a **client**, which displays them in real time. This example is optimized for **low latency** and can be extended for high-performance use cases (e.g., gaming, remote desktop).

---

## **1. Project Setup**
### **Prerequisites**
- Rust installed ([rustup.rs](https://rustup.rs/))
- On Linux, install development libraries:
  ```bash
  sudo apt install libx11-dev libwayland-dev
  ```

---

## **2. Create the Rust Project**
```bash
mkdir rust_screen_stream
cd rust_screen_stream

# Server (captures screen & sends frames)
cargo new server
cd server

# Client (receives & renders frames)
cd ..
cargo new client
```

---

## **3. Server Implementation (`server/src/main.rs`)**
The server captures the screen and sends raw frames over TCP.

```rust
use scrap::{Capturer, Display};
use std::io::Error;
use tokio::net::TcpListener;
use tokio::io::AsyncWriteExt;

#[tokio::main]
async fn main() -> Result<(), Error> {
    // Initialize screen capture
    let display = Display::primary()?;
    let mut capturer = Capturer::new(display)?;
    
    // Start TCP server
    let listener = TcpListener::bind("127.0.0.1:5000").await?;
    println!("Server running on 127.0.0.1:5000");
    
    // Accept client connection
    let (mut socket, _) = listener.accept().await?;
    println!("Client connected!");

    // Capture & send frames in a loop
    loop {
        let frame = capturer.frame()?;
        socket.write_all(&frame).await?;
    }
}
```

### **Dependencies (`server/Cargo.toml`)**
```toml
[dependencies]
scrap = "0.5"          # Screen capture
tokio = { version = "1.0", features = ["full"] }  # Async networking
```

---

## **4. Client Implementation (`client/src/main.rs`)**
The client receives frames and renders them in a window.

```rust
use pixels::{Pixels, SurfaceTexture};
use winit::event_loop::EventLoop;
use winit::window::WindowBuilder;
use tokio::net::TcpStream;
use tokio::io::AsyncReadExt;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Connect to the server
    let mut stream = TcpStream::connect("127.0.0.1:5000").await?;
    println!("Connected to server!");

    // Create a window
    let event_loop = EventLoop::new();
    let window = WindowBuilder::new()
        .with_title("Rust Screen Stream (Client)")
        .build(&event_loop)?;

    // Initialize pixel buffer
    let window_size = window.inner_size();
    let surface_texture = SurfaceTexture::new(window_size.width, window_size.height, &window);
    let mut pixels = Pixels::new(window_size.width, window_size.height, surface_texture)?;

    // Main rendering loop
    event_loop.run(move |event, _, control_flow| {
        control_flow.set_poll();

        match event {
            winit::event::Event::MainEventsCleared => {
                // Read frame data from server
                let frame = pixels.frame_mut();
                let mut buf = vec![0; frame.len()];

                // Blocking read (for simplicity; use async in production)
                tokio::runtime::Runtime::new().unwrap().block_on(async {
                    stream.read_exact(&mut buf).await.unwrap();
                });

                // Update and render
                frame.copy_from_slice(&buf);
                pixels.render().unwrap();
            }
            _ => (),
        }
    });
}
```

### **Dependencies (`client/Cargo.toml`)**
```toml
[dependencies]
winit = "0.28"         # Window management
pixels = "0.13"        # Pixel rendering
tokio = { version = "1.0", features = ["full"] }  # Async networking
```

---

## **5. Running the Example**
### **Terminal 1 (Server)**
```bash
cd server
cargo run --release
```
- The server starts capturing the screen and waits for a client.

### **Terminal 2 (Client)**
```bash
cd client
cargo run --release
```
- The client connects to the server and displays the stream in a window.

---

## **6. Optimizations (Going Beyond RDP)**
To **beat RDP in speed and quality**, consider:

| Optimization | Implementation |
|-------------|----------------|
| **UDP instead of TCP** | Lower latency, but requires error handling |
| **Hardware Acceleration** | Use `wgpu` or `vulkano` for GPU rendering |
| **Video Compression** | Encode frames with `ffmpeg-next` (H.264/HEVC) |
| **Frame Differencing** | Only send changed pixels to reduce bandwidth |
| **Dynamic FPS Adjustment** | Adjust based on network conditions |

### **Example: Switching to UDP**
```rust
// Server (UDP)
use tokio::net::UdpSocket;
let socket = UdpSocket::bind("127.0.0.1:5000").await?;
socket.send_to(&frame, "127.0.0.1:5001").await?;

// Client (UDP)
let socket = UdpSocket::bind("127.0.0.1:5001").await?;
let mut buf = vec![0; 65507]; // Max UDP packet size
socket.recv_from(&mut buf).await?;
```

---

## **7. Troubleshooting**
| Issue | Fix |
|-------|-----|
| **`scrap` fails on Linux** | Install `libx11-dev` (`sudo apt install libx11-dev`) |
| **High CPU usage** | Limit FPS with `std::thread::sleep(Duration::from_millis(16))` (60 FPS) |
| **Laggy stream** | Use **UDP + frame compression** (`ffmpeg-next`) |

---

## **Conclusion**
This example provides a **basic real-time screen streaming system** in Rust. To **surpass RDP**, implement:
- **UDP transport** (lower latency)
- **GPU acceleration** (faster rendering)
- **Video compression** (smaller data size)

For a **production-ready solution**, consider libraries like:
- **Parsec** (low-latency streaming)
- **WebRTC** (browser-compatible streaming)
- **GStreamer** (advanced video processing)

Would you like help extending this for **gaming or remote desktop** use cases? 🚀