#!/usr/bin/node
// rectangle class

function Rectangle (w, h) {
  if (parseInt(w) > 0 && parseInt(h) > 0) {
    this.width = w;
    this.height = h;

    this.print = function () {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(parseInt(this.width)));
      }
    };

    this.rotate = function () {
      this.width = [this.height, this.height = this.width][0];
    };

    this.double = function () {
      this.width *= 2;
      this.height *= 2;
    };
  }
}

module.exports = {Rectangle};
