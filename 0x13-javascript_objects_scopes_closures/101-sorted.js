#!/usr/bin/node
//

const dict = require('./101-data').dict;
const obj = {};

Object.keys(dict).forEach(function(key) {
  if (dict[key] in Object.keys(obj)) {
    obj[dict[key]].push(key)
  } else {
    obj[dict[key]] = [];
    obj[dict[key]].push(key)
  }
});

console.log(obj);
