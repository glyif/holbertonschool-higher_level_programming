#!/usr/bin/node
// add function

let a = parseInt(process.argv[2]);
let b = parseInt(process.argv[3]);

/**
 * add two numbers
 * @param {Int} a
 * @param {Int} b
 * @return {Int} a + b
 */
function add (a, b) {
  return a + b;
}

if (isNaN(a) || isNaN(b)) {
  console.log(NaN);
} else {
  console.log(add(a, b));
}
