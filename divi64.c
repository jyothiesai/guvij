#include <stdio.h>
 
void main()
{
    int  num, dec = 0, base = 1, rem;
    scanf("%d", &num);
    while (num > 0)
    {
        rem = num % 10;
        dec= dec + rem * base;
        num = num / 10 ;
        base = base * 2;
    }
    if(dec%64==0)
    {
    	printf("yes");
    }
    else{
    	printf("no");
    }
}
