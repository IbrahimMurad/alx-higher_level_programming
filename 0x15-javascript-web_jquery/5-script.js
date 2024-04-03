$('DIV#add_item').on('click', function addElement (event) {
  const new_element = '<li>Item</li>';
  $('UL.my_list').append(new_element);
});
