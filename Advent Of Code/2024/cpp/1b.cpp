#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main() {
  vector<int> firstList;
  map<int, int> secondList;

  int num;
  // list is either 0 or 1
  int list = 0;

  while (cin >> num) {
    // cout << list << '\n';
    if (list == 0) {
      list = 1;
      firstList.push_back(num);
    } else {
      list = 0;
      // if num exists in the map, increment it
      if (secondList.find(num) != secondList.end()) {
        secondList[num] += 1;
      } else {
        secondList[num] = 1;
      }
    }
  }

  int total = 0;

  for (int i = 0; i < firstList.size(); i++) {
    int occurances = secondList[firstList[i]];
    // cout << firstList[i] << " occurances: " << occurances << '\n';
    total += firstList[i] * occurances;
  }

  cout << total;

  return 0;
}