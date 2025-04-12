#include <iostream>
#include <map>
#include <string>

using namespace std;

int main() {
    map<int, int> scores;
    int n; cin >> n;
    cin.ignore();
	for (int i = 0; i < n; i++) {
		int score = 0;
		string curr;
		getline(cin, curr);
		for (int z = 0; z < curr.length(); z++) {
			// cout << curr[z] << '\n';
			string nextTwo = (string(1, curr[z]) + string(1, curr[z + 1]));
			if (nextTwo == "AO" || nextTwo == "OA") {
					score += 4;
					score += 1;
			} else if (nextTwo == "OB" || nextTwo == "BO") {
					score += 9;
					score += 1;
			} else if (nextTwo == "BG" || nextTwo == "GB") {
					score += 9;
					score += 1;
			} else if (nextTwo == "GR" || nextTwo == "RG") {
					score += 4;
					score += 1;
			} else {
				// That means that it's one character
				if (curr[z] == 'A' || curr[z] == 'R') {
					score += 1;
				} else if (curr[z] == 'O' || curr[z] == 'G') {
					score += 3;
				} else if (curr[z] == 'B') {
					score += 6;
				}
				if (curr[z + 1] == '+') {
					score += 2;
					z += 2;
				} else {
					z += 1;
				}
				// cout << score << '\n';
				continue;
			}
			if (curr[z + 2] == '+') {
				score += 2;
				z += 3;
			} else {
				z += 2;
			}
			// cout << score << '\n';
		}
		scores[i + 1] = score; 
		// cout << "OUT\n";
	}
	string full = "";
	for (int i = 0; i < n; i++) {
		int person = -1;
		int max = -1;
		for (auto score : scores) {
			if (score.second != -1 && score.second > max) {
				max = score.second;
				person = score.first;
				// cout << score.second << '\n';
		  	}
		}
		full += to_string(person) + "-" + to_string(scores[person]);
		scores[person] = -1;
		if (i != n-1) {
			full += " ";
		}
		// cout << "---\n";
	}
	cout << full;
	//cout << score.first << " is: " << score.second << "\n";
 	return 0;
}