#include <iostream>
#include <vector>
#include <cmath>
#include <string>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<long> cowHeights;

    for (int i = 0; i < n; i++)
    {
        long cowHeight; // changed from int to long
        cin >> cowHeight;
        cowHeights.push_back(cowHeight);
    }

    for (int z = 0; z < m; z++)
    {
        long currCandyCane; // changed from int to long
        long heightEaten = 0; // changed from int to long

        cin >> currCandyCane;

        for (int i = 0; i < cowHeights.size(); i++)
        {
            if (cowHeights[i] >= heightEaten)
            {
                long leftOver = currCandyCane - heightEaten;
                long amountEaten = min(leftOver, cowHeights[i] - heightEaten); // changed from int to long
                cowHeights[i] += amountEaten;
                heightEaten += amountEaten;
            }
        }
    }

    for (int z = 0; z < cowHeights.size(); z++)
    {
        cout << cowHeights[z] << '\n';
    }
    return 0;
}