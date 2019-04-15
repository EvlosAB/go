docker run --restart=always -d -p 5000:5000 -e "MYSQL_DATABASE=go" -e "MYSQL_USER=user" -e "MYSQL_PASSWORD=password" -e "MYSQL_HOST=db" -e "MYSQL_PORT=3306" go:latest
