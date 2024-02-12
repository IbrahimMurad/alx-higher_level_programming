#!/usr/bin/node

const myList = process.argv.slice(2);
const listLength = myList.length;
for (let i = 0; i < listLength; i++) {
  myList[i] = parseInt(myList[i]);
}
let beggest = myList[0];
for (const num of myList) {
  if (num > beggest) {
    beggest = num;
  }
}
myList.splice(myList.indexOf(beggest), 1);
beggest = myList[0];
for (const num of myList) {
  if (num > beggest) {
    beggest = num;
  }
}
if (listLength === 0 || listLength === 1) {
  console.log(0);
} else {
  console.log(beggest);
}
