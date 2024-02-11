// Source: https://usaco.guide/general/io

#include <vector>
#include <string>
#include <iostream>
using namespace std;

int main() {
	freopen("speeding.in", "r", stdin);
	// the following line creates/overwrites the output file
	freopen("speeding.out", "w", stdout);

	int n, m; cin >> n >> m;

	std::vector<int> speedLimit = {};
	std::vector<int> bessieSpeeds = {};
	for (int z = 0; z < n; z++) {
		int length, speed; cin >> length >> speed;
		int count = length;
		// cout << count << '\n';
		while (count > 0) {
			count--;
			// cout << count << " test\n";
			speedLimit.push_back(speed);
		}
	}

	for (int z = 0; z < n; z++) {
		int length, speed; cin >> length >> speed;
		int count = length;
		// cout << count << '\n';
		while (count > 0) {
			count--;
			// cout << count << " test\n";
			bessieSpeeds.push_back(speed);
		}
	}

	for (int i = 0; i < speedLimit.size(); i++) {
        // cout << speedLimit[i] << "\n";
    }
    // cout << endl;

	std::vector<int> overLimits = {}; 

	for (int i = 0; i < 100; i++) {
		if (speedLimit[i] < bessieSpeeds[i]) {
			overLimits.push_back(bessieSpeeds[i] - speedLimit[i]);
		}
	}

	cout << *max_element (overLimits.begin (), overLimits.end ());
	
	// for (int i = 0; i < 100; i++) {
	// 	std::vector<int> v = {};
	// }
}
