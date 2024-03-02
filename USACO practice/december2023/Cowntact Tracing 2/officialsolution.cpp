#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using std::cout;
using std::endl;
using std::vector;

int main() {
    int cow_num;
    std::cin >> cow_num;
    vector<char> cows(cow_num);
    for (char& c : cows) {
        std::cin >> c;
    }

    int curr_run = 0;
    vector<int> sick_runs;
    for (int i = 0; i < cow_num; i++) {
        if (cows[i] == '0') {
            sick_runs.push_back(curr_run);
            curr_run = 0;
        } else {
            curr_run++;
        }
    }
    sick_runs.push_back(curr_run);

    int max_days = INT32_MAX;
    for (int i = 0; i < sick_runs.size(); i++) {
        if (sick_runs[i] == 0) {
            continue;
        }
        if (i == 0 || i == sick_runs.size() - 1) {
            max_days = std::min(max_days, sick_runs[i] - 1);
        } else {
            max_days = std::min(max_days, (sick_runs[i] - 1) / 2);
        }
    }

    int min_sick = 0;
    for (int i = 0; i < sick_runs.size(); i++) {
        min_sick += std::ceil((double)sick_runs[i] / (2 * max_days + 1));
    }

    cout << min_sick << endl;
}