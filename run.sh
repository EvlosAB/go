docker run --restart=always -d -p 5000:5000 -e "MYSQL_DATABASE=go" -e "MYSQL_USER=user" -e "MYSQL_PASSWORD=pass" -e "MYSQL_HOST=host" -e "MYSQL_PORT=3306" go:latest
