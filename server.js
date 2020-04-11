const http = require('http');

const hostname = '172.19.0.11';
const port = 3000;

function between(min, max) {  
  return Math.floor(
    Math.random() * (max - min + 1) + min
  )
}

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  var number = between(10, 200);
  res.end(number + '\n');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
