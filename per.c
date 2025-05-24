#include <stdio.h>
#include <math.h>
#include <stdbool.h>
int main()
{
	int n=28, sum=1;
	for (int i=1; i<sqrt(n)+1; i++)
	{
		if (i>1 n%i==0)
		{
			sum+=i;
			if (i*i!=n && n/i<n)
			{
				sum+=n/i;
			}
		}
	}
	bool per=(n>1 && sum==n);
	if (per)
	{
		printf("perfect no");
	}
	else
	{
		printf("not perfect");
	}
	return 0;
}
