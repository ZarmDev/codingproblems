#include <iostream>
#include <set>

using namespace std;

int main() {
  multiset<int> firstList;
  multiset<int> secondList;

  int num;
  // list is either 0 or 1
  int list = 0;

  while (cin >> num) {
    // cout << list << '\n';
    if (list == 0) {
      list = 1;
      firstList.insert(num);
    } else {
      list = 0;
      secondList.insert(num);
    }
  }

  multiset<int>::iterator itr = firstList.begin();
  multiset<int>::iterator itr2 = secondList.begin();
  int total = 0;
  while (itr != firstList.end()) {
    // cout << abs(*itr - *itr2) << '\n';
    total += abs(*itr - *itr2);
    itr++;
    itr2++;
  }

  cout << total;

  return 0;
}