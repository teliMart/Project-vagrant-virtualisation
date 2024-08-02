<<<<<<< HEAD
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|


  # Configuration du serveur d'application
  config.vm.define "app_server" do |app|
    app.vm.box = "ubuntu/bionic64"
    app.vm.network "private_network", ip: "192.168.33.11"
=======
Vagrant.configure("2") do |config|

  # Configuration du serveur d'application
  config.vm.define "app_server" do |app|
    app.vm.box = "ubuntu/bionic64"
    app.vm.network "private_network", ip: "192.168.33.10"
>>>>>>> 286a8375ba18b5139a39fb333bde7a1c72e528c1
    app.vm.synced_folder ".", "/vagrant", disabled: true
    app.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
    end
<<<<<<< HEAD
    app.vm.provision "shell", path: "provision_app_server.sh"
    app.vm.provision "shell", path: "provision_db_server.sh"
    app.vm.synced_folder "./projetAlumni22", "/home/vagrant/projetAlumni22"
  end

# Configuration du serveur de base de données
  config.vm.define "db_server" do |db|
    db.vm.box = "ubuntu/bionic64"
    db.vm.network "private_network", ip: "192.168.33.12"
    db.vm.synced_folder ".", "/vagrant", disabled: true
    db.vm.provider "virtualbox" do |vb|
      vb.memory = "4096"
    end
    db.vm.provision "shell", path: "provision_db_server.sh"
  end

# Configuration du serveur web
    config.vm.define "web_server" do |web|
      web.vm.box = "ubuntu/bionic64"
      web.vm.network "private_network", ip: "192.168.33.10"
      web.vm.synced_folder ".", "/vagrant", disabled: true
      web.vm.synced_folder "./projetAlumni22/AgenceLuxe/static", "/home/vagrant/projetAlumni22/static"
      web.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
    end
      web.vm.provision "shell", path: "provision_web_server.sh"
  end

end
=======
    app.vm.provision "shell", inline: <<-SHELL
      set -x
      sudo apt-get update
      sudo apt-get install -y python3-pip python3-dev libpq-dev
      sudo apt-get install -y virtualenv
      sudo apt-get install -y nginx
      sudo apt-get install -y git
      sudo apt-get install -y postgresql-client
      cd /home/vagrant/projetAlumni22
      virtualenv venv
      source venv/bin/activate
      pip install -r requirements.txt
      python manage.py migrate
      python manage.py collectstatic --noinput
    SHELL
    app.vm.synced_folder "./projetAlumni22", "/home/vagrant/projetAlumni22"
  end

  # Configuration du serveur de base de données
  config.vm.define "db_server" do |db|
    db.vm.box = "ubuntu/bionic64"
    db.vm.network "private_network", ip: "192.168.33.11"
    db.vm.synced_folder ".", "/vagrant", disabled: true
    db.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
    end
    db.vm.provision "shell", inline: <<-SHELL
      set -x
      sudo apt-get update
      sudo apt-get install -y postgresql postgresql-contrib
      sudo -u postgres psql -c "CREATE USER vagrant WITH PASSWORD 'password';"
      sudo -u postgres psql -c "ALTER ROLE vagrant SET client_encoding TO 'utf8';"
      sudo -u postgres psql -c "ALTER ROLE vagrant SET default_transaction_isolation TO 'read committed';"
      sudo -u postgres psql -c "ALTER ROLE vagrant SET timezone TO 'UTC';"
      sudo -u postgres psql -c "CREATE DATABASE myproject;"
      sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE myproject TO vagrant;"
    SHELL
  end

end

>>>>>>> 286a8375ba18b5139a39fb333bde7a1c72e528c1
