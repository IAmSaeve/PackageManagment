# Express echo server

Just a simple Express server that responds to HTTP POST requests.  
Server is listening on `0.0.0.0` port `7000` with `/echo` as suffix.

## Install dev

Run `npm i` then use the `npm start` or `node server.js` commands.

## Docker
When inside the root dir execute the following:  
`docker build -t seb/echo-server .`  
`docker run -d -p 7000:7000 seb/echo-server:latest`

**NB: "seb" can be any name**

To inspect echos received, `docker attach ContainerID` can be used.