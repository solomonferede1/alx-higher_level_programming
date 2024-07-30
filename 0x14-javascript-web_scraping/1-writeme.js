#!/usr/bin/node

const fs = require('fs');

// Get the file path from command-line arguments
const filePath = process.argv[2];
const string = process.argv[3];

// Read the file content
fs.writeFile(filePath, string, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
