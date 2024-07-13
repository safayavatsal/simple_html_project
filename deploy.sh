#deploy.sh

#!/bin/zsh

# Stop nginx
sudo brew services stop nginx

# Remove existing project directory
sudo rm -rf /usr/local/var/www/*

# Clone the latest code
git clone https://github.com/safayavatsal/simple_html_project.git /usr/local/var/www/

# Restart nginx
sudo brew services start nginx
