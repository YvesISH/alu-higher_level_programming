#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length === 2) {
  console.log(args[0] + 'is' + args[1]);
} else {
  console.log('please provide exactly 2 arguments');
}
