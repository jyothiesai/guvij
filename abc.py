#jyothi
s=raw_input()
l=len(s)
a=s.count('a')
b=s.count('b')
c=a+b
if(l==c or l-c==1):
  print("yes")
else:print("no")
