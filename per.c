#include <stdio.h>
#include <stdbool.h>
int main()
{
	int n=28, sum=1, i=1;
	while (++i<n)
	{
		if (n%i==0)
		{
			sum+=i;
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
