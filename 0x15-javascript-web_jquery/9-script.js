/* global $ */
$.get('//hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
  $('DIV#hello').text(data.hello);
});
