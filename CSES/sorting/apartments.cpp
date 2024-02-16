// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;

int main() {
	int numOfApplicants, numOfApartments, difference; cin >> numOfApplicants >> numOfApartments >> difference;
	vector<int> desiredApartmentSizes;
	for (int i = 0; i < numOfApplicants; i++) {
		int listItem; cin >> listItem;
		// cout << listItem;
		desiredApartmentSizes.push_back(listItem);
	}
	vector<int> apartmentSizes;
	for (int i = 0; i < numOfApartments; i++) {
		int listItem; cin >> listItem;
		// cout << listItem;
		apartmentSizes.push_back(listItem);
	}

	int applicantsThatCanGetApartment = 0;

	// loop through desired arpartment sizes and check if it corresponds with any in the actual aprtment sizes
	for (int i = 0; i < numOfApartments; i++) {
		for (int z = 0; z < (int) desiredApartmentSizes.size(); z++) {
			// if the desired size is higher than x-k and lower than x+k
			if ((apartmentSizes[i] - difference) >= (desiredApartmentSizes[z]) && ((apartmentSizes[i] + difference) <= (desiredApartmentSizes[z]))) {
				// also make sure it's not already taken
				apartmentSizes[i] = -10;

				applicantsThatCanGetApartment++;
			}
		}
	}

	cout << applicantsThatCanGetApartment;
}
