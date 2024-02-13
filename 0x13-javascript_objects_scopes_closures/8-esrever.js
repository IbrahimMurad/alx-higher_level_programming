#!usr/bin/node

exports.esrever = function (list) {
  const tempArray = [];
  for (const element of list) {
    tempArray.unshift(element);
  }
  return tempArray;
};
