#!/bin/bash
python3-venv venv
source venv/bin/activate

sudo apt install python3-pytest

# Docker
sudo apt-get update
sudo apt install curl -y
curl https://get.docker.com | sudo bash

# Docker-compose
sudo apt update
sudo apt install -y curl jq

version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

