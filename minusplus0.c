#include <stdio.h>

int main(void) {
	int n,i,j=0;
	scanf("%d",&n);
	int arr[n],e[100];
	for(i=0;i<n;i++)
	{
		scanf("%d",&arr[i]);
	}
	for(i=0;i<n;i++)
	{
		for(j=i+1;j<n;j++)
		{
			if(arr[i]+arr[j]==0|| arr[i]+arr[j]==-1)
			{
				printf("%d %d",arr[i],arr[j]);
				break;
			}
		}
	}
	return 0;
}
