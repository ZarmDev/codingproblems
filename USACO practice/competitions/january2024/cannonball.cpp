// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;

int main() {
	int lengthOfNumberLine, startingLocation; cin >> lengthOfNumberLine >> startingLocation;
	vector<pair<int, int>> numberLine(lengthOfNumberLine);

	for (int i = 0; i < lengthOfNumberLine; i++) {
		int q, value; cin >> q >> value;
		// cout << "(" << q << ", " << value << ")" << '\n';
		numberLine[i + 1] = make_pair(q, value);
	}
	// numberLine.erase(numberLine.begin());

	int bessiesCurrentLocation = startingLocation;
	// k is power
	int power = 1;
	// 1 is forward, -1 is backwards
	int direction = 1;
	int targetsHit = 0;
	vector<int> alreadyHitTargets;

	for (int i = 0; i < 100; i++) {
		// cout << bessiesCurrentLocation << '\n';
		// if at any point, is she out of the number line, break
		if (!(bessiesCurrentLocation >= 1 && bessiesCurrentLocation <= lengthOfNumberLine)) {
			// cout << "success" << '\n';
			break;
		}
		// first check what q is 1 or 0
		pair currentPlace = numberLine[bessiesCurrentLocation];
		// jumpad! k += value at number line and reverse direction
		// cout << currentPlace.first << " <- q value " << '\n';
		// The first should be q which is jumpad if 0 and otherwise target if 1
		// cout << currentPlace.first << " " << currentPlace.second << '\n';
		if (currentPlace.first == 0) {
			// cout << '1' << '\n';
			direction *= -1;
			power += currentPlace.second;
		} else if (currentPlace.first == 1) {
			// power should remain the same as well as the direction
			// make sure bessies current location not in alreadyhit
			// cout << bessiesCurrentLocation << "SUS" << '\n';
			bool alreadyInTargets = (find(alreadyHitTargets.begin(), alreadyHitTargets.end(), bessiesCurrentLocation) != alreadyHitTargets.end());
			// make sure that she can even break the target
			// if her power is > than the value there
			bool canBreakTarget = (power >= currentPlace.second);
			// cout << "[" << !alreadyInTargets << ", " << canBreakTarget << "] \n";
			if (!(alreadyInTargets) && canBreakTarget) {
				targetsHit += 1;
				// for (int z = 0; z < alreadyHitTargets.size(); z++) {
				// 	cout << "(" << alreadyHitTargets[z] << ") ";
				// }
				alreadyHitTargets.push_back(bessiesCurrentLocation);
			}
		}

		// regardless of what was there, move based on the power and direction
		// cout << power << " " << direction << '\n';
		bessiesCurrentLocation += (power * direction);
	}

	cout << targetsHit;

}
