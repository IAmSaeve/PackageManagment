const express = require('express');
const http = require('http');
const bodyParser = require('body-parser');
const app = express();
const port = 7000;
const addr = '0.0.0.0';

app.use(bodyParser.text({
  type: function (req) {
    return 'text';
  }
}));

app.post('/echo', function (req, res) {
  console.log('REQ', req.body);
  res.status(200).send(req.body)
});

http.createServer(app).listen(port, addr, () => {
  console.log(`Listening on: http://${addr}:${port}/post`)
});
