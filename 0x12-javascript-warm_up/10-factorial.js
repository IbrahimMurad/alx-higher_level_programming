#!/usr/bin/node

function fac (n) {
  if (!n || n === 1) {
    return 1;
  } else {
    return n * fac(n - 1);
  }
}
console.log(fac(parseInt(process.argv[2])));
