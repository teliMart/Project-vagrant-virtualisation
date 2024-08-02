#!/usr/bin/env bash

# Mettre à jour les paquets et installer PostgreSQL
sudo apt-get update
sudo apt-get install -y postgresql postgresql-contrib

# Configurer PostgreSQL
sudo -u postgres psql -c "CREATE USER vagrant WITH PASSWORD 'password';"
sudo -u postgres psql -c "ALTER ROLE vagrant SET client_encoding TO 'utf8';"
sudo -u postgres psql -c "ALTER ROLE vagrant SET default_transaction_isolation TO 'read committed';"
sudo -u postgres psql -c "ALTER ROLE vagrant SET timezone TO 'UTC';"
sudo -u postgres psql -c "CREATE DATABASE myproject;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE myproject TO vagrant;"

# Modifier pg_hba.conf pour ajouter une nouvelle ligne
echo "host    all             all             192.168.33.11/32        md5" | sudo tee -a /etc/postgresql/10/main/pg_hba.conf

# Modifier postgresql.conf pour ajouter listen_addresses = '*'
sudo sed -i "/^#listen_addresses = 'localhost'/c\listen_addresses = '*'" /etc/postgresql/10/main/postgresql.conf

# Redémarrer PostgreSQL pour appliquer les modifications
sudo systemctl restart postgresql
