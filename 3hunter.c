#include <stdio.h>

int main(void) {
	int n,i,c=0;
	scanf("%d",&n);
	int arr[n];
	for(i=0;i<n;i++)
	{
		scanf("%d",&arr[i]);
	}
	for(i=0;i<n;i++)
	{
		if(arr[i]==i)
		{
			printf("%d ",i);
			c++;
		}
	}
	if(c==0)
	{
		printf("-1");
	}
	return 0;
}
