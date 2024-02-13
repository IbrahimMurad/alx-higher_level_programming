#!/usr/bin/node

const dict = require('./101-data').dict;
const listOfKeys = [];
for (const key in dict) {
  listOfKeys.unshift(key);
}
console.log(listOfKeys);
const listOfValues = [];
for (const key of listOfKeys) {
  listOfValues.unshift(dict[key]);
}
console.log(listOfValues);
const newDict = {};
for (let i = 0; i < listOfKeys.length; i++) {
  newDict[listOfValues[i]] = [];
}
for (let i = 0; i < listOfKeys.length; i++) {
  newDict[listOfValues[i]].unshift(listOfKeys[i]);
}
console.log(newDict);
