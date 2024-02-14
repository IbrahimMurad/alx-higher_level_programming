#!/usr/bin/node

const dict = require('./101-data').dict;
const listOfKeys = [];
for (const key in dict) {
  listOfKeys.push(key);
}
const listOfValues = [];
for (const key of listOfKeys) {
  listOfValues.push(dict[key]);
}
const newDict = {};
for (const key of listOfValues) {
  newDict[key] = [];
}
for (let i = 0; i < listOfKeys.length; i++) {
  newDict[listOfValues[i]].push(listOfKeys[i]);
}
console.log(newDict);
