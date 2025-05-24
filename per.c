#include <stdio.h>
#include <math.h>
#include <stdbool.h>
int main()
{
	int n=28, sum=1, i=2;
	while (i*i<n)
	{
		if (n%i==0)
		{
			sum+=i;
			if(i*i!=n)
			{
				sum+=n/i;
			}
		}
		i++;
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
