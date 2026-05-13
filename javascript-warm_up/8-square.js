#!/usr/bin/node
const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let square_line = '';
    for (let j = 0; j < num; j++) {
      square_line += 'X';
    }
    console.log(square_line);
  }
}
