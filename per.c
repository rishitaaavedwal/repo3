#include <stdio.h>
#include <stdbool.h>
#include <math.h>
int main()
{
	int n=28, sum=1;
	bool per=false;
	for (int i=2; i*i<=n; i++)
	int n=28, sum=1, i=2;
	while (i*i<n)
	for (int i=2; i<=n/2; i++)
	{
		if (n%i==0)
		{
			sum+=i;
			if (i*i!=n)
			{
				sum+=n/i;
			}
		}
		if(sum>n)
		{
			break;
		}
			if(i*i!=n)
			{
				sum+=n/i;
			}
		}
	}
	if (n>1 && sum==n) per=true;
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
