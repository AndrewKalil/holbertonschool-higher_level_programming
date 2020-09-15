#!/usr/bin/node
// prints value of arguements

if (process.argv.length === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
