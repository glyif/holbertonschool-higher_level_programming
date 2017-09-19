#!/usr/bin/node
// args found or not

let args = process.argv;

if (args[2] === undefined) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
