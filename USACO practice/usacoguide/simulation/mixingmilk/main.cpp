#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

int main()
{
	freopen("shell.in", "r", stdin);

	vector<int> capacities;
	vector<int> milkBuckets;

	for (int i = 0; i < 3; i++)
	{
		int c, m;
		scanf("%d %d", &c, &m);
		capacities.push_back(c);
		milkBuckets.push_back(m);
	}

	// compare capacity and the added amount of milkbucket + amount from other bucket
	int order = 0;
	int maxOrder = 2;

	for (int i = 1; i < 100; i++)
	{
		int lastPos = i - 1;
		// if on first order, last order is last element
		if (i == 0)
		{
			lastPos = maxOrder;
		}
		if (order == maxOrder)
		{
			order = 0;
			lastPos = 0;
		}
		else
		{
			order += 1;
		}

		printf("%d %d", lastPos, order);
		printf("\n");

		milkBuckets[i] = min(capacities[i], milkBuckets[i] + milkBuckets[lastPos]);
	}

	// freopen("mixmilk.out", "w", stdout);

	// for (int i = 0; i < milkBuckets.size(); i++)
	// {
	// 	printf("%d ", milkBuckets[i]);
	// }
	// printf("\n");
}