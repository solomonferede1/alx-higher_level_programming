#!/usr/bin/node
const process = require('process');
let i = 0;

if (!(isNaN(parseInt(process.argv[2])))) {
  while (i < parseInt(process.argv[2])) {
    console.log('x'.repeat(parseInt(process.argv[2])));
    i++;
  }
} else {
  console.log('MissingMissing size');
}
