#include <stdio.h>

int main(void) {
	int n,i,j;
	scanf("%d",&n);
	int arr[n];
	for(i=0;i<n;i++)
	{
		scanf("%d",&arr[i]);
	}
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			if(i!=j && arr[i]==arr[j])
			{
				break;
			}
		}
		if(j==n)
		{
			printf("%d",arr[i]);
		}
	}
	return 0;
}
