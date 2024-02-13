#!/usr/bin/node

class Square extends require('./5-square') {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let line = '';
        for (let j = 0; j < this.width; j++) {
          line += c;
        }
        console.log(line);
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
