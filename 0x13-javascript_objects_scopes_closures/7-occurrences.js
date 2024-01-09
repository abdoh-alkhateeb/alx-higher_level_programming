#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nbOccurences = 0;

  for (const item of list) {
    if (item === searchElement) {
      nbOccurences++;
    }
  }

  return nbOccurences;
};
