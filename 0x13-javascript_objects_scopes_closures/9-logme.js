#!/usr/bin/node
// log me
let counter = 0;

function logMe (string) {
  counter++;
  console.log('%d: %s', counter, string);
}

module.exports = {logMe};
