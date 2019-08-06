#include<stdio.h>
 
int main() {
   char str1[30], str2[30];
   int i;
   scanf("%s %s",str1,str2);
   i = 0;
   while (str1[i] == str2[i] && str1[i] != '\0')
      i++;
   if (str1[i] == str2[i])
      printf("yes");
   else
      printf("no");
 
   return 0;
}
