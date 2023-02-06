#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');

const url = `https://swapi-api.htbn.io/api/films/${args[0]}`;

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const parsedData = JSON.parse(body);
    console.log(parsedData.title);
  }
});
