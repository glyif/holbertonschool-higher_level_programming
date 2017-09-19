#!/usr/bin/node
// square

let tryInt = parseInt(process.argv[2]);

if (isNaN(tryInt)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < tryInt; i++) {
    console.log('X'.repeat(tryInt));
  }
}
