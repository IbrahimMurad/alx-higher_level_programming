#!/usr/bin/node

const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', (err, data1) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data1);
});
