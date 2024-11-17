#include <bits/stdc++.h>
#include <string>
using namespace std;

string evaluate(vector<string> arr) {
	if (arr.size() == 0) {
		string firstItem = arr[0];
		return firstItem;
	}
	// first check and operator
	for (int i = 1; i < (int) arr.size(); i += 2) {
		bool lastItem;
		bool afterItem;
		cout << arr[i + 1];
		break;
		if (arr[i - 1] == "true") {
			lastItem = true;
		} else {
			lastItem = false;
		}
		if (arr[i + 1] == "true") {
			afterItem = true;
		} else {
			afterItem = false;
		}
		bool andoperator = (lastItem && afterItem);
		if (i % 2 != 0 && andoperator == true) {
			if (arr.size() != 1) {
				//
			}
		}
	}
	// bool oroperator = (lastItem || afterItem);
	return "Z";
}

int main() {
	int n, q; cin >> n >> q;
	vector<string> statement;
	for (int i = 0; i < n; i++) {
		string item; cin >> item;
		statement.push_back(item);
		// cout << item << '\n';
	}
	for (int i = 0; i < q; i++) {
		int l, r; cin >> l >> r;
		string expectedValue; cin >> expectedValue;
		// cout << l << " wth " << r << '\n';
		// ###BRUTE FORCE HERE####
		cout << l << r << expectedValue << '\n';
		vector<string> modifedArr = statement;
		// modify segment [l, r]
		for (int t = 0; t < pow(2, statement.size()); t++) {
			modifedArr[t] = "false";
			for (int z = t + 1; z < r - 1; z++) {
				modifedArr[z] = "true";
			}
		}
		evaluate(modifedArr);
	}
	return 0;
}
