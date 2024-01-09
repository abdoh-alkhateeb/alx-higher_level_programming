#!/usr/bin/node
exports.esrever = function (list) {
  const reversedList = [];
  const length = list.length;

  for (let i = length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }

  return reversedList;
};
