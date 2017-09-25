#!/usr/bin/node
// rectangle class

function Rectangle (w, h) {
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }

  this.print = () => {
    for (let i = 0; i < this.height; i++) {
      console.log('#'.repeat(this.width));
    }
  };

  this.rotate = () => {
    this.width = [this.height, this.height = this.width][0];
  };

  this.double = () => {
    this.width = this.width * 2;
    this.height = this.width * 2;
  };
}

module.exports = {Rectangle};
