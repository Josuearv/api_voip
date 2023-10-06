#!/bin/bash

# Instalar Python y las dependencias de FastAPI
sudo yum -y install python3
sudo pip3 install fastapi
mkdir /var/www/ApiServer

# Clonar el código de la aplicación
git clone https://github.com/Josuearv/api_voip.git /var/www/ApiServer
pass = $(cat passwordMysql.log)

# Crear un archivo config.py
echo "DB_HOST = '192.168.1.1'" >> /var/www/ApiServer/app/config.py
echo "DB_PORT = 3306" >> /var/www/ApiServer/config.py
echo "DB_USER = 'user'" >> /var/www/ApiServer/app/config.py
echo "DB_PASSWORD = '$password'" >> /var/www/ApiServer/app/config.py

# Crear un servicio systemd
cat << EOF | sudo tee /etc/systemd/system/fastapi.service
[Unit]
Description=FastAPI App
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=/var/www/appApiServer
ExecStart=/usr/bin/python3 main.py
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# Habilitar y iniciar el servicio systemd
sudo systemctl enable fastapi
sudo systemctl start fastapi
