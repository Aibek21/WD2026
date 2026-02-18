const input = require('fs').readFileSync('/dev/stdin', 'utf8').trim();

// Your code here
const lines = input.split('\n');
const name = lines[0].trim();
const age = lines[1].trim();

const msg = `Hello, ${name}! You are ${age}`;
console.log(msg);