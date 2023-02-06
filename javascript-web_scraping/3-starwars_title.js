#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
request.get(url, (error, result) => {
  error ? console.log(err) : console.log(JSON.parse(result.body).title);
});
