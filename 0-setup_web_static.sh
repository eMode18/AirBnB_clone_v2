#!/usr/bin/env bash
# A script to prepare web_servers for deployment
# Ensure nginx exists, else install it
if [ ! -x /usr/sbin/nginx ]
then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi
# Command to make the required directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
# HTML test file
touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    <h1>Nginx configuration test <h1>
  </body>
</html>" > /data/web_static/releases/test/index.html
# Establish symbolic link between the directories
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# assign user and group ownership to ubuntu
sudo chown -R ubuntu:ubuntu /data
sudo chmod -R 755 /data/
# Update the Nginx to server hbnb_static
sudo sed -i '48 i \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
# Restart nginx
sudo service nginx restart
