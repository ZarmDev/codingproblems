// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;

#include <cstdio>
#include <vector>

void setIO(string s) {
	ios_base::sync_with_stdio(0); cin.tie(0);
	freopen((s+".in").c_str(),"r",stdin);
	freopen((s+".out").c_str(),"w",stdout);
}

int main() {
	setIO("lostcow");
	int farmerJohnPos, BessiePos;
	cin >> farmerJohnPos >> BessiePos;
	int count = 1;
	char operation = '-';
	int newPosition = farmerJohnPos + count;
	count = count * 2;
	vector<int> allPos;
	allPos.push_back(newPosition);
	while (newPosition < BessiePos) {
		newPosition = farmerJohnPos;
		//cout << farmerJohnPos << ' ';
		if (operation == '+') {
			operation = '-';
			newPosition = farmerJohnPos + count;
		} else {
			operation = '+';
			newPosition = farmerJohnPos - count;
		}
		//cout << newPosition << ' ';
		allPos.push_back(newPosition);
		count = count * 2;
		//cout << count << ' ';
	}

	int vectorSum = 0;
	for (auto i = allPos.begin(); i < allPos.end() - 1; ++i) {
		//cout << abs(i[1] - i[0]) << '\n';
		if (i[1] > i[0]) {
			vectorSum = vectorSum + abs(i[1] - i[0]);
		} else {
			vectorSum = vectorSum + abs(i[0] - i[1]);
		}
    }

	cout << vectorSum;
}
