// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
#include <vector>
using namespace std;

void setIO(string s) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	freopen((s + ".in").c_str(), "r", stdin);
	freopen((s + ".out").c_str(), "w", stdout);
}

int main() {
	setIO("shuffle");
	int n; cin >> n;
	
	// first artifically create an array wtih n itmes
	vector<int> originalArray;

	for (int i = 1; i < n + 1; i++) {
		originalArray.push_back(i);
	}

	// for (int i = 0; i < (int) originalArray.size(); i++) {
	// 	cout << originalArray[i] << '\n';
	// }
	// cout << "----------" << '\n';

	vector<int> shuffleLocations;
	// input shuffle
	for (int i = 0; i < n; i++) {
		int curr; cin >> curr;
		shuffleLocations.push_back(curr);
	}

	vector<int> originalIDs;

	for (int i = 0; i < n; i++) {
		int curr; cin >> curr;
		originalIDs.push_back(curr);
	}

	// three shuffles
	for (int t = 0; t < 3; t++) {
		vector<int> temporaryNewArr(5);
		// now SHUFFLE!
		for (int i = 0; i < n; i++) {
			// go from i -> shuffleLocations[i] and reverse: shuffleLocations[i] (3) -> i (2)
			// cout << "originalArray[" << shuffleLocations[i] - 1 << "] = " << originalArray[shuffleLocations[i] - 1] << '\n';
			temporaryNewArr[i] = originalArray[shuffleLocations[i] - 1];
		}
		originalArray = temporaryNewArr;
		// for (int i = 0; i < (int) originalArray.size(); i++) {
		// 	cout << originalArray[i] << '\n';
		// }
		// cout << "------" << '\n';
	}

	// now compare with the cow ID's
	for (int i = 0; i < n; i++) {
		// my braincells werent working writing this
		// cout << "originalIDs[" << originalArray[i] << "] = " << originalIDs[originalArray[i]] << '\n';
		cout << originalIDs[originalArray[i] - 1] << '\n';
	}		
}
