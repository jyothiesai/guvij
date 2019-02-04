#include <stdio.h>
 
int main()
{
  int a ,tot = 0, i, b[100];
  scanf("%d", &a);
  for (i = 0; i <a; i++)
  {
    scanf("%d", &b[i]);
    tot = tot + b[i];
  }
 
  printf("%d", tot);
 
  return 0;
}

