function Fibonacci(n) {
  if(n == 0) {
    return 0;
  }
  else if(n == 1) {
    return 1;
  }
  else {
    return Fibonacci(n - 1) + Fibonacci(n - 2);
  }
}


var max_value = 4000000;
//  Get first value
var a = 2;
var val = Fibonacci(a);
var values = [];

while(val < max_value) {
  //  If even valued add to list
  if(val % 2 == 0) {
    values.push(val);
  }
  //  Get new value
  a++;
  val = Fibonacci(a);
}
//  Find sum
var sum = 0;
for(i = 0; i < values.length; i++) {
  sum += values[i];
}
console.log(sum);
phantom.exit();
