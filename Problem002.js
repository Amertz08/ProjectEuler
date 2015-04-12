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

var a = 1;
var max_value = 1000;
var values = [];
while(Fibonnaci(a) < max_value) {
  if(Fibonnaci(a) % 2 == 0) {
    
  }
}
phantom.exit();
