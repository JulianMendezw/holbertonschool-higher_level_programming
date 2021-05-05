#!/usr/bin/node
const argv = process.argv;
const request = require('request');
const url = argv[2];
const characterID = 18;

let count = 0;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const rbody = JSON.parse(body);
    for (const i of rbody.results) {
      for (const j of i.characters) {
        if (j.search(characterID) > 0) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
