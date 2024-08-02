#!/bin/bash

# Mettre à jour les paquets et installer nginx
sudo apt-get update
sudo apt-get install -y nginx

# Configurer NGINX pour l'équilibrage de charge
sudo bash -c 'cat > /etc/nginx/sites-available/default <<EOF
upstream django_servers {
    server 192.168.33.11:8000;
}

server {
    listen 80;

    location / {
        proxy_pass http://django_servers;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF'

# Configurer Nginx
sudo rm /etc/nginx/sites-enabled/default

cat <<EOL | sudo tee /etc/nginx/sites-available/projetAlumni22
server {
    listen 80;
    server_name 192.168.33.10;

    location / {
        proxy_pass http://192.168.33.11:8000;  # Adresse et port de votre application Django
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }

    location /static/ {
        alias /home/vagrant/projetAlumni22/static/;  # Chemin vers vos fichiers statiques Django
    }

    location /media/ {
        alias /home/vagrant/projetAlumni22/media/;  # Chemin vers vos fichiers media Django
    }
}
EOL

sudo ln -s /etc/nginx/sites-available/projetAlumni22 /etc/nginx/sites-enabled/projetAlumni22
sudo systemctl restart nginx
