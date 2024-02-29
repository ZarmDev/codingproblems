// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
#include <vector>
using namespace std;

int main() {
	int n; cin >> n;
	
	// first artifically create an array wtih n itmes
	vector<int> originalArray(5);

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
			// my braincells werent working writing this
			temporaryNewArr[i] = originalArray[shuffleLocations[i]];
		}
		originalArray = temporaryNewArr;
	}

	// now compare with the cow ID's
	for (int i = 0; i < n; i++) {
		// my braincells werent working writing this
		cout << originalIDs[originalArray[i]];
	}

}
