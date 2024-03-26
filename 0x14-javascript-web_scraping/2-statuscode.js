#!/usr/bin/node

const request = require('request');
const theURL = process.argv[2];

request(theURL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
