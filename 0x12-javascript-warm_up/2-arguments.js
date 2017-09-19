#!/usr/bin/node
// args found or not

let args = process.argv;

if (args.length > 2) {
  if (args.length > 3) {
    console.log('Arguments found');
  } else {
    console.log('Argument found');
  }
} else {
  console.log('No argument');
}
