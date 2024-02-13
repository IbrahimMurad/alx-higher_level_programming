#!/usr/bin/node

const oldList = require('./100-data').list;
const newList = oldList.map((x) => x * oldList.indexOf(x));
console.log(list);
console.log(newList);
