#!/usr/bin/node
// recursive factorial

let num = parseInt(process.argv[2]);

/**
 * factorial recursive function
 * @param num: number to calculate factorial
 */
function factorial (num) {
  if (isNaN(num) || num === 1 || num === 0) {
    return 1;
  }
  return factorial(num - 1) * num;
}

console.log(factorial(num));
