// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;

void setIO(string s) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	freopen((s + ".in").c_str(), "r", stdin);
	freopen((s + ".out").c_str(), "w", stdout);
}

int main() {
	setIO("lostcow");

	int x, y; cin >> x >> y;
	int doubled = 1;
	char sign = '-';
	int distance = 0;
	

	if (y > x) {
		// start as positive +1
		int withSign = 1;
		// bessie is ahead
		int i = 0;
		while (!(x + withSign >= y)) {
			x += withSign;
			// cout << x << '\n';
			if (sign == '-') {
				sign = '+';
				withSign = -doubled;
			} else {
				sign = '+';
				withSign = doubled;
			}
			
			if ((x + withSign >= y)) {
				distance += x - (x - y);
				// cout << x << "-(" << x << "-" << y << ") sus" << distance << '\n';
				break;
			}
			distance += doubled;
			doubled *= 2;


			// cout << "\n" << x << withSign << y << "?";
			// cout << distance;
			if (i > 100) {
				break;
			}
			i++;
		}
		cout << distance;
	} else if (x == y) {
		cout << 0;
		return 1;
	}
	else {
		// bessie is backwards
		// start as positive +1
		int withSign = 1;
		// bessie is ahead
		int i = 0;
		while (!(x + withSign <= y)) {
			x += withSign;
			// cout << x << '\n';
			if (sign == '-') {
				sign = '+';
				withSign = -doubled;
			} else {
				sign = '+';
				withSign = doubled;
			}
			
			if ((x + withSign <= y)) {
				distance += x - (x - y);
				// cout << x << "-(" << x << "-" << y << ") sus" << distance << '\n';
				break;
			}
			distance += doubled;
			doubled *= 2;


			// cout << "\n" << x << withSign << y << "?";
			// cout << distance;
			if (i > 100) {
				break;
			}
			i++;
		}
		cout << distance;
	}
}
