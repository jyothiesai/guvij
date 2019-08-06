#include<stdio.h>
 
int main() {
   char str1[30], str2[30];
   int m,n;
   scanf("%s %s",str1,str2);
   m=strlen(str1);
   n=strlen(str2);
   if (m == n)
      printf("yes");
   else
      printf("no");
 
   return 0;
}
