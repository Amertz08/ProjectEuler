/*
n         - int
returns   - boolean

Takes in an int n and returns true if value is prime
*/
function isPrime(n) {
  for(i = 2; i < n; i++) {
    if(n % i == 0) {
      return false;
    }
  }
  return true;
}
/*
n         - int
returns   - array

Takes in an int and returns and array of factors
from smallest to largest not including 1 or n
*/
function findFactors(n) {
  var f = [];
  for(i = 2; i < n; i++) {
    if(n % i == 0) {
      f.push(i);
    }
  }
  return f
}
var a = 13195;
var factors = findFactors(a);
console.log('Found factors');
console.log(factors);

/*
for(i = 0; i < factors.length; i++) {
  if(isPrime(factors[i])) {
    console.log(factors[i]);
  }
}

for(i = factors.length - 1; i > 1; i--) {
  if(isPrime(factors[i])) {
    console.log(i);
    break;
  }
}
*/
phantom.exit();
