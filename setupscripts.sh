#!/bin/bash
sudo apt install python3-venv
rm -rf venv
python3 -m venv venv
source venv/bin/activate
python3 --version

pip3 install pytest pytest-cov

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

# Install ansible

sudo apt install software-properties-common
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt install ansible
# mkdir -p ~/.local/bin
# echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
# source ~/.bashrc
# sudo apt install python3-pip -y
# pip3 install --user ansible
# ansible --version

type ansible
type ansible-playbook

pip3 install -r requirements.txt
