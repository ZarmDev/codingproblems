// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;
#include <vector>
using std::vector; 

int main() {
	freopen("speeding.in", "r", stdin);
	freopen("speeding.out", "w", stdout);

    int N, M;
	cin >> N >> M;

    //cout << N << ' ' << M << '\n';

	vector<int> speedLimit;
	vector<int> bessieSpeed;

	for (int i = 0; i < N; i++) {
		int N2, N3;
		cin >> N2 >> N3;
		for (int z = 0; z < N2; z++) {
			speedLimit.push_back(N3);
		}
	}
	for (int i = 0; i < M; i++) {
		int N2, N3;
		cin >> N2 >> N3;
		for (int z = 0; z < N2; z++) {
			bessieSpeed.push_back(N3);
		}
	}
	int maxvalue = 0;
	for (int i = 0; i < speedLimit.size(); i++) {
		int sub = (bessieSpeed[i] - speedLimit[i]);
        //cout << sub << ' ';
		if (sub > maxvalue) {
			//cout << sub;
			maxvalue = sub;
		}
    }
    cout << maxvalue;
}