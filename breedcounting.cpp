// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
#include <vector>
using namespace std;

int main() {
	int n, q; cin >> n >> q;

	vector<int> holsteins;
	vector<int> guernseys;
	vector<int> jerseys;
	// generate prefix sum list
	int h = 0;
	int g = 0;
	int j = 0;
	for (int i = 0; i < n; i++) {
		int breedid; cin >> breedid;
		if (breedid == 1) {
			holsteins.push_back(h);
			h += breedid;
		} else if (breedid == 2) {
			guernseys.push_back(g);
			g += breedid;
		} else if (breedid == 3) {
			jerseys.push_back(j);
			j += breedid;
		}
	}

	for (const auto& z : holsteins) {
        std::cout << z << " ";
    }
	cout << '\n';

	for (const auto& z : guernseys) {
        std::cout << z << " ";
    }
	cout << '\n';

	for (const auto& z : jerseys) {
        std::cout << z << " ";
    }
	cout << '\n';

	// then perform queries
	for (int i = 0; i < q; i++) {
		int a, b; cin >> a >> b;
		cout << [holsteins[b] - holsteins[a]] << [holsteins[b] - holsteins[a]] << [holsteins[b] - holsteins[a]];
	}
}
