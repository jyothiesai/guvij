#include <stdio.h>

int main(void) {
	int n,i;
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
		}
	}
	return 0;
}
