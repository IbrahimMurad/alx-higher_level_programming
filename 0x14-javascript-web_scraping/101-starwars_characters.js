#!/usr/bin/node

const request = require('request');
const theURL = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(theURL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const film = JSON.parse(body);
    for (const character of film.characters) {
      request(character, (error1, response1, body1) => {
        if (error1) {
          console.error(error1);
        } else {
          console.log(JSON.parse(body1).name);
        }
      });
    }
  }
});
