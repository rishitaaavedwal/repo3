#include <stdio.h>
#include <stdbool.h>
#include <math.h>
int main()
{
	int n=28, sum=1, i=2;
	while (i<=sqrt(n))
	{
		if (n%i==0)
		{
			sum+=i;
			if (i*i!=n)
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
