// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
#include <vector>
using namespace std;

int main() {
	// You are given an array of n integers, 
	// and your task is to find two values (at distinct positions) whose sum is x.
	int arrsize, targetsum; cin >> arrsize >> targetsum;
	if (arrsize == 1) {
		cout << "IMPOSSIBLE";
		return 0;
	}
	vector<int> values;
	// redundant
	// for (int i = 0; i < arrsize; i++) {
	// 	int listItem; cin >> listItem;
	// 	// cout << listItem;
	// 	values.push_back(listItem);
	// }
	// instead
	for (int i = 0; i < arrsize; i++) { cin >> values[i]; }

	// loop over every possible combination/addition
	// 1 2 3 4 5

	// loop over each array item
	for (int i = 0; i < arrsize; i++) {
		// sum first 1 with other 5, then 2 with other 5...
		for (int z = 0; z < arrsize; z++) {
			// make sure to skip over itself
			if (z == i) {
				continue;
			}
			if (values[i] + values[z] == targetsum) {
				cout << i + 1 << " " << z + 1;
				return 0;
			}
		}
	}

	cout << "IMPOSSIBLE";
}