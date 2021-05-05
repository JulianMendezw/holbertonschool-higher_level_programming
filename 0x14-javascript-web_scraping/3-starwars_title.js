#!/usr/bin/node
const argv = process.argv;
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
