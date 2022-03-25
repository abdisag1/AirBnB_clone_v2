#!/usr/bin/env bash
# sets up the webservers for deployment
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
mkdir -p /data
mkdir /data/web_static
mkdir /data/web_static/releases
sudo mkdir /data/web_static/shared/
mkdir /data/web_static/releases/test
echo "test my servers" | sudo tee /data/web_static/releases/test/index.html
rm -f /data/web_static/current && ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -hr ubuntu:ubuntu /data/
redirect="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "50s|.*|$redirect|" /etc/nginx/sites-enabled/default
sudo service nginix start
