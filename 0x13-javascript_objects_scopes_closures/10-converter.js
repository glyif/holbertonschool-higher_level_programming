#!/usr/bin/node
// converts a number from base 10 to another base passed

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
