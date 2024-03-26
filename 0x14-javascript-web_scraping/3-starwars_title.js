#!/usr/bin/node

const request = require('request');
const episode = process.argv[2];
const theURL = `https://swapi-api.alx-tools.com/api/films/${episode}`

request(theURL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
