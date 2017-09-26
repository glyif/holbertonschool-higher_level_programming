#!/usr/bin/node
// log me
let counter = 0;

function logMe (string) {
  console.log(counter + ': ' + string);
  counter++;
}

module.exports = {logMe};
