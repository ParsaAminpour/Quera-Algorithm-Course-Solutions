#include<iostream>
#include<algorithm>
using namespace std;

const int maxn = 5000 + 2;

int main()
{
	int n, k, c[maxn], money; 
	
	cin >> n >> k;
	for(int i = 0; i < n; i++)
		cin >> c[i];
	
	if(k >= 3)
	{
		money = c[0];
		for(int i = 0; i < n; i++)
			money = min(money, c[i]);
	}
	else if(k == 2)
	{
		int maxs[maxn], maxe[maxn];
		
		maxs[0] = c[0];
		for(int i = 1; i < n; i++)
			maxs[i] = max(c[i], maxs[i - 1]);

		maxe[n - 1] = c[n - 1];
	       	for(int i = n - 2; i >= 0; i--)
			maxe[i] = max(c[i], maxe[i + 1]);	
		
		money = 5000;
		for(int i = 1; i < n; i++)
			money = min(money, min(maxs[i - 1], maxe[i]));
	}
	else
	{
		money = c[0];
		for(int i = 0; i < n; i++)
			money = max(money, c[i]);		
	}

	cout << money;
	return 0;
}