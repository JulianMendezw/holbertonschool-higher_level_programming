#!/usr/bin/node
const argv = process.argv;
const request = require('request');
const url = argv[2];
const characterID = 18;
const characList = 'https://swapi-api.hbtn.io/api/people/' + characterID + '/';
let count = 0;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    for (let i = 0; results[i]; i++) {
      if (results[i].characters.indexOf(characList) > -1) {
        count = count + 1;
      }
    }
    console.log(count);
  }
});
