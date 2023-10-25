#!/usr/bin/node
/* Made by laila */
const url = process.argv[2];
const request = require('request');

request(url, { method: 'GET' }, (err, { statusCode }) => {
	  if (err) return console.log(err);
	  console.log(`code: ${statusCode}`);
});
