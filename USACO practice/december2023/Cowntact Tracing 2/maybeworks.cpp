#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    string finalState;
    cin >> finalState;

    vector<bool> accountedFor(n, false);
    int initiallyInfected = 0;

    for (int i = 0; i < n; ++i) {
        if (finalState[i] == '1' && !accountedFor[i]) {
            ++initiallyInfected;
            if (i + 1 < n) accountedFor[i + 1] = true;
            if (i + 2 < n) accountedFor[i + 2] = true;
        }
    }

    cout << initiallyInfected;
    return 0;
}