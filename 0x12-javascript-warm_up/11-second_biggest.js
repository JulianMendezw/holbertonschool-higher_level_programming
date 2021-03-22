#!/usr/bin/node
const argv = process.argv;
let max;
const arraycopy = [];

function SecondMax (array) {
  if (array.length <= 3) {
    return 0;
  } else {
    for (let i = 2; i < array.length; i++) {
      arraycopy.push(parseInt(array[i])); /* copy the original array and parse to Integer */
    }
    max = Math.max.apply(null, arraycopy); /* get the max of the array */
    arraycopy.splice(arraycopy.indexOf(max), 1); /* remove max from the array */
    return Math.max.apply(null, arraycopy); /* get the 2nd max */
  }
}
console.log(SecondMax(argv));
