#!/usr/bin/node

const fs = require('fs');

// Get the file path from command-line arguments
const filePath = process.argv[1];


// Read the file content
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
