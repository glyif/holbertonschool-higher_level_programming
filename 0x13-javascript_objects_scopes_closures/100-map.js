#!/usr/bin/node
// factor index

const list = require('./100-data').list;
let index = 0;

console.log(list);

console.log(list.map(function(number) {
  let newNumber = number * index;
  index += 1;
  return newNumber;
}));
