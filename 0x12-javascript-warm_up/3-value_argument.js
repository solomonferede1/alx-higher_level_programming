#!/usr/bin/node
const process = require('process');

const argsLength = (process.argv).length;
if (argsLength <= 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
