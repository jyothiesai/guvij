#include <stdio.h>
#include<math.h>
int main(void) {
	int n,sum=0,rem;
	scanf("%d",&n);
	while(n>0)
	{
		rem=n%10;
		sum=sum+pow(rem,4);
		n=n/10;
	}
	printf("%d",sum);
	return 0;
}
