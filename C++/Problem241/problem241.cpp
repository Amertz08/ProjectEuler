#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

//  Function prototypes
int sigma(int n);
vector<int> find_factors(int n);
int sum(vector<int> l);

int main() {
  double ans, x;
  long max = pow(10, 18);
  int a;

  for(double i = 1; i < 12; i++) {
    ans = sigma(i) / i;
    a = ans - 0.5;
    cout << "i: " << i << " ans: " << ans
    << " a: " << a << endl;
  }

  return 0;
}

vector<int> find_factors(int n) {
  vector<int> l;
  for(int i = 1; i <= n; i++) {
    if(n % i == 0) {
      l.push_back(i);
    }
  }
  return l;
}

int sum(vector<int> l) {
  int s = 0;
  for(int i = 0; i < l.size(); i++) {
    s += l[i];
  }
  return s;
}

int sigma(int n) {
  vector<int> l = find_factors(n);
  return sum(l);
}
