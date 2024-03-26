#!/usr/bin/node

const request = require('request');
const theURL = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

function printCharacter (character) {
  return new Promise((resolve) => {
    request(character, (error1, response1, body1) => {
      resolve(JSON.parse(body1).name);
    });
  });
}

async function printInOrder (characters) {
  for (const character of characters) {
    const name = await printCharacter(character);
    console.log(name);
  }
}

request(theURL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const film = JSON.parse(body);
    printInOrder(film.characters);
  }
});
