#include <iostream>
#include <vector>
using namespace std;

//  Function prototypes
int sigma(int n);
vector<int> find_factors(int n);
int sum(vector<int> l);

int main() {
  int x;
  double ans;


  cout << "Enter a value: " << endl ;
  cin >> x;
  ans = sigma(x) / x;
  cout << ans << endl;
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
