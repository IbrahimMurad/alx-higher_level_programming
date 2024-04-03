document.addEventListener('DOMContentLoaded', function () {
  const newElement = '<li>Item</li>';
  const theList = $('UL.my_list');

  const addBtn = $('DIV#add_item');
  const removeBtn = $('DIV#remove_item');
  const clearBtn = $('DIV#clear_list');

  addBtn.on('click', function () {
    theList.append(newElement);
  });

  removeBtn.on('click', function () {
    theList.children().last().remove();
  });

  clearBtn.on('click', function () {
    theList.empty();
  });
});
