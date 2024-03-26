#!/usr/bin/node

const request = require('request');
const theURL = process.argv[2].replace('films', 'people/18');

request(theURL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).films;
    console.log(films.length);
  }
});
