#!/usr/bin/env bash
# Script de setup RPi - placeholder
# NOTA: revise antes de executar. Este script deve rodar como root (sudo).
set -euo pipefail

echo "Atualizando sistema..."
sudo apt update && sudo apt upgrade -y

echo "Instalando dependências básicas (mosquitto, docker, nodejs, python3)..."
sudo apt install -y mosquitto mosquitto-clients docker.io docker-compose nodejs npm python3 python3-pip

echo "Habilitando e inicializando mosquitto..."
sudo systemctl enable mosquitto
sudo systemctl start mosquitto

echo "Instalar Node-RED (opcional)..."
# npm i -g --unsafe-perm node-red

echo "Instalação básica concluída. Para deploy completo, rode docker-compose na pasta deployment/docker."
