use tokio::net::TcpListener;
use rsa::{Pkcs1v15Encrypt, RsaPrivateKey, RsaPublicKey};

// Servidor envia sinal para verificar se o client está acessivel
// Se o Sinal voltar assindo, OK
// Se o pacote demorar + 4 Segundos, retorna que o client está inacessivel 

fn main(){

}

