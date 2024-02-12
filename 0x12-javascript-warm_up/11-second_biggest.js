#!/usr/bin/node

const myList = process.argv.slice(2).sort();

if (myList.length === 0) {
  console.log(0);
} else {
  console.log(myList);
}
