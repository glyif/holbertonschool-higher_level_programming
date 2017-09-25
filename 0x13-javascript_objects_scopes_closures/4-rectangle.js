#!/usr/bin/node
// rectangle class

function Rectangle (w, h) {
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }

  this.print = function () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  };

  this.rotate = function () {
    this.width = [this.height, this.height = this.width][0];
  };

  this.double = function () {
    this.width = this.width * 2;
    this.height = this.width * 2;
  };
}

module.exports = {Rectangle};
