//jyothi
#include <stdio.h>
int main(void)
{
	int n,k,a[100],count=0,i;
	scanf("%d",&n);
	scanf("%d",&k);
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=0;i<n;i++)
	{
		if(a[i]==k)
		{
			printf("Yes");
			count=1;
		}
	}
	if(count==0)
	{
		printf("No");
	}
	return 0;
}
