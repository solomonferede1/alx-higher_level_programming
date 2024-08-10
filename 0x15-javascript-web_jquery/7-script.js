/* global $ */
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  type: 'GET',
  success: (result) => $('DIV#character').text(result.name)
});
