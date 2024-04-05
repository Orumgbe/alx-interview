#!/usr/bin/node
// Prints all characters of a Star Wars movie
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function Names (i, url, chars, len) {
  if (i === len) {
    return;
  }
  request.get(url, function (err, response, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      i++;
      Names(i, chars[i], chars, len);
    }
  });
}

request.get(url, function (err, response, body) {
  if (!err) {
    const characters = JSON.parse(body).characters;
    const len = characters.length;
    Names(0, characters[0], characters, len);
  }
});
