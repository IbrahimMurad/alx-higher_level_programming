#!/usr/bin/node

const myList = process.argv.slice(2).sort();
const listLength = myList.length;
if (listLength === 0) {
  console.log(0);
} else if (listLength === 1) {
  console.log(myList[0]);
} else {
  console.log(myList[listLength - 2]);
}
