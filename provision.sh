#!/bin/bash

# Update package list and install dependencies
sudo apt-get update
sudo apt-get install -y python3-pip python3-dev libpq-dev
sudo apt-get install -y virtualenv nginx

# Navigate to project directory
cd /home/vagrant/projetAlumni22

# Create virtual environment and activate it
virtualenv venv
source venv/bin/activate

# Install project dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Configure Gunicorn
pip install gunicorn
gunicorn --workers 3 --bind unix:/home/vagrant/projetAlumni22.sock projetAlumni22.wsgi:application &

# Configure Nginx
sudo cp /vagrant/nginx_projetAlumni22 /etc/nginx/sites-available/projetAlumni22
sudo ln -s /etc/nginx/sites-available/projetAlumni22 /etc/nginx/sites-enabled
sudo rm /etc/nginx/sites-enabled/default
sudo service nginx restart


USE mysql;
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password123';
FLUSH PRIVILEGES;
