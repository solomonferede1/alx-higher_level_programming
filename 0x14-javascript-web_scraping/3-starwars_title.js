#!/usr/bin/node

const request = require('request');

// Get the movie ID (episode number) from command-line arguments
const movieId = process.argv[2];

// Construct the URL for the API endpoint
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Perform a GET request to fetch the movie details
request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    // Successfully received the response
    console.log(`Title: ${body.title}`);
  } else {
    // Handle non-200 status codes
    console.error(`Failed to fetch data. Status Code: ${response.statusCode}`);
  }
});
