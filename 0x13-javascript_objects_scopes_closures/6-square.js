#!/usr/bin/node
// Define a square class inherits from Rectangle

const oldSquare = require('./5-square');
class Square extends oldSquare {
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.height));
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
