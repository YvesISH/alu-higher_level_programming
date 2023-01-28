#!/usr/bin/node
const factorial = (n) => {
  if (isNaN(n)) {
    return 1;
  }
  if ( n === 1 || n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
};

const num = parseInt(process.argv[2]);
console.log(factorial(num));
