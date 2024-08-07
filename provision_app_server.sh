#!/bin/bash

# Mettre à jour la liste des paquets
sudo apt-get update

# Installer pip3 s'il n'est pas déjà installé
sudo apt-get install -y python3-pip

# Installer les dépendances nécessaires
sudo apt-get install -y python3-pip libpq-dev

# Désinstaller Django
sudo pip3 uninstall -y Django

# Installer les paquets Python requis
sudo pip3 install django==2.2.28
sudo pip3 install djangorestframework
sudo pip3 install django-phonenumber-field
sudo pip3 install psycopg2

# Installer les dépendances supplémentaires pour Pillow
sudo apt-get install -y zlib1g-dev libjpeg-dev libpng-dev libfreetype6-dev liblcms2-dev libopenjp2-7-dev libtiff5-dev tk-dev tcl-dev

# Installer Pillow
python3 -m pip install Pillow
