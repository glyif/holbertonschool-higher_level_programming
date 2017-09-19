#!/usr/bin/node
// run functions multiple times

/**
 * callMeMoby, repeats function x times
 * @param x: times to repeat function
 * @param theFunction: function to repeat
 */
function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

module.exports = {callMeMoby};
