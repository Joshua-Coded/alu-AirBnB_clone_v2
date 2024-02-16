#!/bin/bash

# Install Nginx if it's not already installed
sudo apt update
sudo apt install -y nginx || { echo "Failed to install Nginx"; exit 1; }

# Ensure SSH is installed and running (OpenSSH server)
sudo apt install -y openssh-server || { echo "Failed to install OpenSSH server"; exit 1; }
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
</html>" | sudo tee /data/web_static/releases/test/index.html || { echo "Failed to create fake HTML file"; exit 1; }

# Create a symbolic link, after removing if it already exists
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/ || { echo "Failed to change ownership of /data/"; exit 1; }

# Update the Nginx configuration to serve the content
nginx_conf="/etc/nginx/sites-available/default"
sudo sed -i '/listen 80 default_server;/a location /hbnb_static { alias /data/web_static/current/; }' $nginx_conf || { echo "Failed to update Nginx configuration"; exit 1; }

# Restart Nginx to apply the changes
sudo systemctl restart nginx || { echo "Failed to restart Nginx"; exit 1; }

# Success message
echo "Setup completed successfully."
exit 0
