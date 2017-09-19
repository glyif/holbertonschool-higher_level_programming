#!/usr/bin/node
// second biggest

function secondLargest (array) {
  let max = Math.max.apply(null, array);

  array.splice(array.indexOf(String(max)), 1);

  return Math.max.apply(null, array);
}

let intArray = process.argv.slice(2);

if (intArray.length < 2) {
  console.log('0');
} else {
  console.log(secondLargest(intArray));
}
