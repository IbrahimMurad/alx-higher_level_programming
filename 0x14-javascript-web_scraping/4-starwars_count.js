#!/usr/bin/node

const request = require('request');
const theURL = process.argv[2];
const WedgeAntilles = 'https://swapi-api.alx-tools.com/api/people/18/';
let count = 0;

request(theURL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    for (const film of films) {
      for (const character of film.characters) {
        if (character.endsWith('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
