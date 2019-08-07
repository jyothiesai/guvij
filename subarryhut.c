#include <stdio.h>

int main(void) {
	int m,n,i,j,count=0;
	scanf("%d %d",&m,&n);
	int arr[m],arr1[n];
	for(i=0;i<m;i++)
	{
		scanf("%d",&arr[i]);
	}
	for(j=0;j<n;j++)
	{
		scanf("%d",&arr1[i]);
	}
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			if(arr[i]==arr1[j])
			{
				count+=1;
			}
		}
	}
	if(count==n)
	{
		printf("No");
	}
	else{
		printf("Yes");
	}
	return 0;
}
