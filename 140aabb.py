#jyothi
s=raw_input()
a=len(s)
n=0
for i in s:
  if (i=="a" or i=="b"):
    n=n+1
if(n==a):
 print("yes")
else:
  print("no")
