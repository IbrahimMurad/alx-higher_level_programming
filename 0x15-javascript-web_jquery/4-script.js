
$('DIV#toggle_header').on('click', function toggleClass (event) {
  const myheader = $('header');
  if (myheader.hasClass('red')) {
    myheader.removeClass('red');
    myheader.addClass('green');
  } else if (myheader.hasClass('green')) {
    myheader.removeClass('green');
    myheader.addClass('red');
  }
});
