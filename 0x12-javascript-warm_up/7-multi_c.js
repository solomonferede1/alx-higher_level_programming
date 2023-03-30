#!/usr/bin/node
const process = require('process');

let i = 0;

if (!(isNaN(parseInt(process.argv[2])))) {
  while (i < parseInt(process.argv[2])) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
