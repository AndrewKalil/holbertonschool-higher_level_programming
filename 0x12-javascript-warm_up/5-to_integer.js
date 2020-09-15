#!/usr/bin/node
// converts a number to an integer

if (process.argv.length === 2 || isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
