#!/usr/bin/node

const request = require('request');

// Get the URL from command-line arguments
const url = process.argv[2];

// Perform a GET request
request.get(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(response.statusCode);
  }
});
