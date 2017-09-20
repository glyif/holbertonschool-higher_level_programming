#!/usr/bin/node
// callback function incrementation

/**
 * addMeMaybe - callback function that increments number
 * @param number: number to increment
 * @param theFunction: function to call back
 */
function addMeMaybe (number, theFunction) {
  theFunction(number + 1);
}

module.exports = {addMeMaybe};
