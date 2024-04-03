document.addEventListener('DOMContentLoaded', function () {
  const transBtn = $('#btn_translate');
  const hello = $('#hello');
  const langCodeInput = $('#language_code');

  function translate () {
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + langCodeInput.val(), function (data) {
      hello.html(data.hello);
    });
  }

  transBtn.on('click', translate);

  langCodeInput.on('keypress', function (e) {
    if (e.key === 'Enter') {
      translate();
    }
  });
});
