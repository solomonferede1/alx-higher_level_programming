/* global $ */
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  success: (data) => {
    const movies = data.results;
    movies.forEach((movie) => {
      $('<li></li>').text(movie.title).appendTo('UL#list_movies');
    });
  }
});
