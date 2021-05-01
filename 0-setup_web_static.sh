#!/usr/bin/env bash
# sets up a server for deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo 'This has been a test' > /data/web_static/releases/test/index.html
ln -fs /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i
