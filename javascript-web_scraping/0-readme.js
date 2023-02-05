#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], (err, contents) => {
  err ? console.log(err) : console.log(contents.toString());
});
