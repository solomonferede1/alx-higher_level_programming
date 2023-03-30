#!/usr/bin/node

const len = process.argv.length;

if (len <= 3) {
  console.log(0);
} else {
  console.log(process.argv.sort((a, b) => a - b).reverse()[1]);
}
