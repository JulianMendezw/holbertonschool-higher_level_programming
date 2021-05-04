#!/usr/bin/node
const argv = process.argv;

const request = require('request');
request(argv[2], function (error, response) {
  if (error) {
    console.error('code: ', error); // Print the error if one occurred
  } else {
    console.log('code: ', response.statusCode); // Print the response status code if a response was received
  }
});
