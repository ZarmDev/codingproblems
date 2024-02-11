#include <iostream>
#include <vector>
#include <cmath>
#include <string>
using namespace std;
template <typename T>

void printVector(vector<T> v)
{
    for (auto element : v)
    {
        cout << "[" << element << "] " << '\n';
    }
}

int main()
{
    /* make cin not tied with cout meaning cin meaning that
    you have to "flush" manually. Basically, just don't use
    scanf, printf and cin and cout in the same file if you use it */
    ios::sync_with_stdio(false);
    /* Improves runtime if you are using cin and cout together
    I don't know why... */
    cin.tie(nullptr);

    // Read amount of cows
    int n;
    cin >> n;

    // Read finalState
    string finalState;
    cin >> finalState;
    // cout << finalState << "\n";

    // first, read the input
    /*
    6
    011101
    */

    // assume 11111 has an answer of 1 to prevent problems
    // check if no zeros
    // if (finalState.find('0') == string::npos)
    // {
    //     cout << 1 << endl;
    //     return 0;
    // }
    // if (finalState.find('1') == string::npos)
    // {
    //     cout << 0 << endl;
    //     return 0;
    // }

    // then, simulate all clumps going backwards:
    // count the amount of "occurances" or clumps
    // then, reverse engineer the center of the clump
    // or, on odd 1's, you can ASSUME they are neccesary since lone 1's have not "expanded"
    // ## DEEXPAND ##
    vector<char> finalStateList;
    vector<string> clumps;

    std::string delimiter = "0";        // the character to split by

    for (int i = 0; i < finalState.length(); i++)
    {
        finalStateList.push_back(finalState[i]);
    }

    size_t pos = 0;    // the current position in the string
    std::string token; // the current substring
    while ((pos = finalState.find(delimiter)) != std::string::npos)
    {
        token = finalState.substr(0, pos); // get the substring from 0 to pos
        if (!token.empty())
        {                               // ignore empty substrings
            clumps.push_back(token); // add the substring to the vector
        }
        finalState.erase(0, pos + delimiter.length()); // erase the processed part of the string
    }
    if (!finalState.empty())
    { // add the remaining part of the string if not empty
        clumps.push_back(finalState);
    }

    // printVector(clumps);

    // ok, now, go through each possible occurance and de-expand the clump (n + 1, n - 1)
    // when, all the clumps are now lone 1's and there are only lone 1's, expand every single one
    // until the list looks like '11111'
    // then, count the number of nights it took

    // 001001 - 0 night
    // we are trying to get 011101
    // if we attempted this, it would be 011111
    // then 111111
    // SO, it's impossible to get that night and the original number of cows is correct

    // in the case of say, 110111
    // we deexpand and get 100010
    // then, we try to expand the clumps
    // In one night we get 110111
    // Therefore, it takes 1 night
    // Then, 1 night = 2 cows (not sure if always the case?)
    // So, answer is 2?
    // Also, mathematically, 110111 is gonna be '11' and '111' where '11' takes one night
    // (Since it's odd, 2 infected / 2 = 1 and since it's not a float, no need to round, but it would be rounded
    // up if neccesary)
    // And '111' takes one night (Since it's odd, 3 infected / 2 = 1.5 and rounded down is 1)
    float minCowSum = 0;
    for (auto item : clumps)
    {
        // temporary exception - if we find a lone 1 I think it means it's impossible and original count is right
        if (item == "1")
        {
            minCowSum = 0;
            for (auto item2 : clumps)
            {
                minCowSum += item2.length();
                // cout << item2 << " " << item2.length() << '\n';
            }
            cout << minCowSum << endl;
            return 0;
        }

        // cout << item << " " << item.length() << " + " << ((item.length() % 2)) << '\n';
        // If the clump is on the edges
        if ((item.length() % 2) == 0)
        { // If clump is even (round up)
            cout << "\nEVEN" << '\n';
            // Get the nights that it takes
            float nights = ceil(item.length() / 4.0);
            // formula
            float formula = item.length() / ((2 * nights) + 1);
            // new formula
            // float formula = item.length() / ((1 * nights) + 2);
            int minCowsPerClump = ceil(formula);
            // cout << item.length() << " n " << minCowsPerClump << '\n';
            minCowSum += minCowsPerClump;
        }
        else if ((item.length() % 2) != 0)
        { // Clump is odd (round down)
            cout << "\nOdd" << '\n';
            cout << item << '\n';
            // Get the nights it takes
            float nights = round(item.length() / 2.0);
            // formula
            float minCowsPerClump = round(item.length() / (2 * nights + 1));
            cout << nights << " n " << minCowsPerClump << '\n';
            minCowSum += minCowsPerClump;
        }
    }

    // in the case of multiple 1's like: 11111110111100
    // we count the clump of '1111111' and since it's 7, it has to be '0111110' and then '0011100' and so on
    // it takes 1 -> '0111110' 2-> '0011100' 3-> '0001000' [3 NIGHTS]
    // so generally, on uneven clumps, you can say 7/2=3.5 and round down to 3
    // therefore, we can generalize it as amountofinfected/2 rounded down

    // Cleaner debug console
    // cout << '\n';
    // cout << '\n';
    // cout << '\n';
    // cout << '\n';
    cout << minCowSum << endl;
    return 0;
}