// in a clump
    // bool inClump = false;
    // string tempClump = "";

    // for (int i = 0; i < finalState.length(); i++)
    // {
    //     if (finalState[i] == '1')
    //     {
    //         inClump = true;
    //     }
    //     // If in a clump
    //     if (inClump && finalState[i] != '0')
    //     {
    //         // then, add to the temporary clump
    //         tempClump += finalState[i];
    //     }
    //     if (finalState[i] == '0' || i == finalState.length() - 1)
    //     {
    //         inClump = false;
    //         clumps.push_back(tempClump);
    //         tempClump = "";
    //     }
    //     finalStateList.push_back(finalState[i]);
    // }
    // clumps.erase(clumps.begin());
    // printVector(clumps);
    // 011101 -> split clumps of 1