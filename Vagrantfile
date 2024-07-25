# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  
  # Configuration du serveur d'application
  config.vm.define "app_server" do |app|
    app.vm.box = "ubuntu/bionic64"
    app.vm.network "private_network", ip: "192.168.33.11"
    app.vm.synced_folder ".", "/vagrant", disabled: true
    app.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
    end
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
