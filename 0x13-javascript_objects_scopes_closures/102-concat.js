#!/usr/bin/node

const fs = require('fs');
let file1Conent;
fs.readFile(process.argv[2], 'utf-8', (err, data1) => {
	if (err) {
		console.log(err);
		return;
	}
	fs.readFile(process.argv[3], 'utf-8', (err, data2) => {
		if (err) {
			console.log(err);
			return;
		}
		fs.writeFile(process.argv[4], data1 + data2, (err) => {
			if (err) {
				console.log(err);
				return;
			}
		});
	});
});
