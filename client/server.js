


var express = require('express');
    server = express();
    path = require("path"),

server.use(express.static(__dirname));
server.use(express.static(path.join(__dirname, "public")));
server.use(express.static(path.join(__dirname, "bower_components")));

var port = process.env.PORT || 8081;
server.listen(port);
console.log('Use port ' + port + ' to connect to this server');

exports = module.exports = server;
