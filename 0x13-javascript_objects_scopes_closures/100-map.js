#!/usr/bin/node

let list = require('./100-data.js').list;

const newList = list.map((n, index) => n * index)
console.log(list);
console.log(newList);
