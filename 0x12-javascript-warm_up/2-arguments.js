#!/usr/bin/node
const argv= process.argv;
if (!argv[2])
	console.error('No argument');
if (argv.length == 3)
	console.log('Argument found');
else
	console.log('Arguments found');
