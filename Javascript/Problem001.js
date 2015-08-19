var values = [];
var sum = 0;

for(n = 1; n <= 1000; n++) {
  if(n%3 == 0) {
    values.push(n);
  }
  else if(n%5 == 3) {
    values.push(n);
  }
}

for(n = 1; n < values.length; n++) {
  sum += values[n];
}
console.log(sum);
phantom.exit();
