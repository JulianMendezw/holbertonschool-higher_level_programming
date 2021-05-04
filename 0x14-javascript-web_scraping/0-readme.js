#!/usr/bin/node
const fs = require('fs');
const pathFile = process.argv;

fs.readFile(pathFile[2], 'utf8', function (err, data) {
  if (err) {
    return console.error(err);
  }

  console.log(data);
});
