#!/usr/bin/node
// print argv amount of times

let tryInt = parseInt(process.argv[2]);

if (isNaN(tryInt)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < tryInt; i++) {
    console.log('C is fun');
  }
}
