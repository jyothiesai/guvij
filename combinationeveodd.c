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
		if(i%2!=0)
		{
			if(arr[i]%2==0)
			{
				e[j]=arr[i];
				j++;
			}
			
		}
		else{
			if(arr[i]%2!=0)
			{
				e[j]=arr[i];
				j++;
			}
		}
	}
	for(i=0;i<j;i++)
	{
		printf("%d ",e[i]);
	}
	return 0;
}
