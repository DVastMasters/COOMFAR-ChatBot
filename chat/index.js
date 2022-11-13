var app = require('express')();
var http = require('http');
var server = http.Server(app)
var io = require('socket.io')(server);
var port = process.env.PORT || 3000;
const urlRobo = "http://127.0.0.1:5000/answer/";

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
});

getAnswerRobot = (msg) => {
  let data = "";

  http.get(urlRobo + msg, (answer) => {
    answer.on("data", (chunk) => {
      data += chunk;
    });

    answer.on("end", () => {
      io.emit('chat message', "COOMFAR: " + data);
    });

  })  
}

io.on('connection', function (socket) {
  socket.on('chat message', function (msg) {
    io.emit('chat message', "Você: " + msg);
    getAnswerRobot(msg);
  });
});

server.listen(port, function () {
  console.log('listening on *:' + port);
});
