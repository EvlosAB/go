# go
go is a service that will let you create links to other URLs so you only have to remember
one keyword. This is particularly good for teams that has URLs that they need to use but
don't want to remember them, write them out or use a bookmark.

This project was inspired by the go link service at Google.

Example: https://go.evlos.se/google will redirect you to Google.

## Usage

### Hosts file
To get the most out of go, put an entry in your computers hosts file and point go to your url.
In our case we would do `go go.evlos.se` and then when we use `go/google` in our browser, we would
be redirected to Google's website.

### Server installation
If you want to run this in docker, use the run file provided (provided you have built the dockerfile beforehand)
https://github.com/EvlosCo/go/blob/master/run.sh.

Obviously replace the environment variables with your mysql credentials. You can also build the docker image with
https://github.com/EvlosCo/go/blob/master/build.sh.

### Disclaimer
Make sure that you dedicate an IP that listens to port 80. Reverse proxies etc won't work as your hosts file will use
the ip and not take in to account what magic a reverse proxy does.

### Adding/deleting/modifying links
To create, modify or delete links you will need to use the go-cli (https://github.com/EvlosCo/go-cli) or you can interact
with the API directly with a tool like Postman or even a web browser.

## Roadmap
* Tokens and protected endpoints
