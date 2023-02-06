#!/usr/bin/node
const file = process.argv.slice(2);
const request = require('request');

const url = `https://swapi-api.htbn.io/api/films/${file[0]}`;

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const parsedData = JSON.parse(body);
    console.log(parsedData.title);
  }
});
