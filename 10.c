//jyothisridhhar
#include <stdio.h>
int main()
{
int n,k,a[4],i;
scanf("%d",&n);
scanf("%d",&k);
for(i=0;a[i]!='\0';i++)
{
scanf("%d",&a[i]);
if(a[i]==k)
{
printf("%d",k);
}
}
return 0;
}
