$('DIV#add_item').on('click', function addElement (event) {
  const newElement = '<li>Item</li>';
  $('UL.my_list').append(newElement);
});
