#!/usr/bin/env bash
# CICD

# Install Nginx if it's not already installed
sudo apt update
sudo apt install -y nginx

# Ensure SSH is installed and running (OpenSSH server)
sudo apt install -y openssh-server
sudo systemctl enable ssh
sudo systemctl start ssh

# Ensure the directory structure exists
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link, after removing if it already exists
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content
nginx_conf="/etc/nginx/sites-available/default"
sudo sed -i '/listen 80 default_server;/a location /hbnb_static { alias /data/web_static/current/; }' $nginx_conf

# Restart Nginx to apply the changes
sudo systemctl restart nginx
