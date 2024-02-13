#!/usr/bin/node

const oldList = require('./100-data').list;
let i = 0;
const newList = oldList.map((x) => x * i++);
console.log(oldList);
console.log(newList);
