#!/usr/bin/node
const argv= process.argv;
if (argv.length < 3)
	console.error('No argument');
else if (argv.length == 3)
	console.log('Argument found');
else
	console.log('Arguments found');
