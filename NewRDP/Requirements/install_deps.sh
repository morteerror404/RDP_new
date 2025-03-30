#!/bin/env bash

# Função de loading animado
show_loading() {
    local pid=$1
    local message="$2"
    local delay=0.1
    local spin='-\|/'
    local i=0
    
    # Esconde o cursor
    tput civis
    
    while kill -0 "$pid" 2>/dev/null; do
        i=$(( (i+1) %4 ))
        printf "\r[%c] %s..." "${spin:$i:1}" "$message"
        sleep "$delay"
    done
    
    # Restaura o cursor e limpa a linha
    tput cnorm
    printf "\r%s\r" " "
}

# Função para verificar e instalar pacotes
install_package() {
    local package="$1"
    local install_cmd="$2"
    
    echo -n "Verificando $package..."
    
    if dpkg -l | grep -q "^ii  $package"; then
        echo " já instalado."
        return 0
    else
        echo " instalando..."
        
        # Executa o comando de instalação em background
        $install_cmd > /dev/null 2>&1 &
        local pid=$!
        
        show_loading "$pid" "Instalando $package"
        
        wait "$pid"
        if [ $? -eq 0 ]; then
            echo "$package instalado com sucesso!"
            return 0
        else
            echo "Falha ao instalar $package!" >&2
            return 1
        fi
    fi
}

# Atualizar lista de pacotes primeiro
echo "Atualizando lista de pacotes..."
apt update -y > /dev/null 2>&1 &
show_loading $! "Atualizando lista de pacotes"

# Instalar pacotes necessários
install_package "libx11-dev" "apt install libx11-dev -y"
install_package "libwayland-dev" "apt install libwayland-dev -y"

# Instalar Rust
echo "Verificando Rust..."
if command -v rustc > /dev/null; then
    echo "Rust já está instalado."
else
    echo "Instalando Rust..."
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y > /dev/null 2>&1 &
    show_loading $! "Instalando Rust"
    
    # Adicionar Rust ao PATH
    if [ -f "$HOME/.cargo/env" ]; then
        source "$HOME/.cargo/env"
        echo "Rust instalado com sucesso!"
    else
        echo "Falha ao instalar Rust!" >&2
        exit 1
    fi
fi

echo "Todas as dependências estão instaladas!"