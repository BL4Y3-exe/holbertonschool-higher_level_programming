#!/usr/bin/node
const args = prosses.argv.lenght - 2;

if (args == 0) {
  console.log('No arguments');
} else if (args == 1) {
  console.log('Argument fonund');
} else {
  console.log('Arguments found');
}
