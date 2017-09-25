#!/usr/bin/node
// square from rectangle

const Rectangle = require('./4-rectangle').Rectangle;

function Square (size) {
  Rectangle.call(this, size, size);
}

module.exports = {Square};
