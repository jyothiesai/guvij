#include <stdio.h>

int main(void) {
	int a,i;
	scanf("%d",&a);
	if(a>2)
	{
		for(i=1;i<=a;i++)
		{
			if(a%i==0)
			{
				printf("%d ",i);
			}
		}
	}
	else{
		printf("1");
	}
	return 0;
}
