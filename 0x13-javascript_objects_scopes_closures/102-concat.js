#!/usr/bin/node

console.log(process.argv);
const fs = require('fs');
let file1Conent;
fs.readFile('./filaA', 'utf8', (err, data) => {
	if (err) {
		console.log(err);
		return;
	}
	console.log(data);
	file1Conent = data;
});
console.log(file1Conent);
