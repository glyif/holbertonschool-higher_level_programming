#!/usr/bin/node
// argv to int

let tryInt = parseInt(process.argv[2]);

if (isNaN(tryInt)) {
  console.log('Not a number');
} else {
  console.log('My number: %d', tryInt);
}
