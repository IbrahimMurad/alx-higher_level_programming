document.addEventListener('DOMContentLoaded', function () {
  const transBtn = $('INPUT#btn_translate');
  const hello = $('DIV#hello');

  transBtn.on('click', function translate () {
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + $('INPUT#language_code').val(), function (data) {
      hello.html(data.hello);
    });
  });
});
