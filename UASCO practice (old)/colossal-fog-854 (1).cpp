#include <bits/stdc++.h>
#include <string>
using namespace std;

string evaluate(vector<string> arr) {
	if (arr.size() == 0) {
		string firstItem = arr[0];
		cout << "WIRIRWREWOTE";
		return "true";
	}
	// first check and operator
	for (int i = 1; i < (int) arr.size(); i += 2) {
		bool lastItem;
		bool afterItem;
		cout << arr[i + 1];
		if (i != 0 && arr[i - 1] == "true") {
			lastItem = true;
		} else {
			lastItem = false;
		}
		if (i + 1 != (int) arr.size() && arr[i + 1] == "true") {
			afterItem = true;
		} else {
			afterItem = false;
		}
		bool andoperator = (lastItem && afterItem);
		if (i % 2 != 0 && andoperator == true) {
			if (arr.size() != 1) {
				vector<string> newArr = vector<string>(arr.begin() + i, arr.end() - (i - 1));
				evaluate(newArr);
			}
		}
	}
	// then check or operator
	for (int i = 1; i < (int) arr.size(); i += 2) {
		bool lastItem;
		bool afterItem;
		cout << arr[i + 1];
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
		bool oroperator = (lastItem || afterItem);
		if (i % 2 != 0 && oroperator == true) {
			if (arr.size() != 1) {
				vector<string> newArr = vector<string>(arr.begin() + i, arr.end() - (i - 1));
				evaluate(newArr);
			}
		}
	}
	// bool oroperator = (lastItem || afterItem);
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
		cout << l << " " << r << " " << expectedValue << '\n';
		// modify segment [l, r]
		for (int t = l; t < r; t++) {
			vector<string> modifedArr = statement;
			modifedArr[t] = "true";
			string test = evaluate(modifedArr);
			// cout << test;
		}
		for (int t = l; t < r; t++) {
			vector<string> modifedArr = statement;
			modifedArr[t] = "false";
			string test = evaluate(modifedArr);
			// cout << test;
		}
	}
	return 0;
}
