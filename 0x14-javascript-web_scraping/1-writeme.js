#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;

fs.open(argv[2], 'a', (err, fd) => {
  if (err) {
    console.error(err);
  } else {
    fs.write(fd, argv[3], (err, bytes) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
