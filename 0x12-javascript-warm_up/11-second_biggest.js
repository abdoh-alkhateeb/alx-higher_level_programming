#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let max = Number.NEGATIVE_INFINITY;
  for (let i = 2; i < process.argv.length; i++) {
    if (process.argv[i] > max) {
      max = process.argv[i];
    }
  }
  console.log(max);
}
