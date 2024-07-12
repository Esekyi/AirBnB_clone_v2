#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get install -y nginx

sudo mkdir -p /data/web_static/shared /data/web_static/releases/test
echo "<html>
	<head>
		<title>Test</title>
	</head>
	<body>
		<h1>Test</h1>
	</body>
</html>" | sudo tee /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/server_name _;/a \\tlocation /hbnb_static { alias /data/web_static/current/; }' /etc/nginx/sites-available/default
sudo service nginx restart
