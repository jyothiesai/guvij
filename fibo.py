#jyothi
x=input()
a=0
b=1
count=0
if(x==0):
	print(a)
else:
    while(count<x):
        nexterm= a+b
        a=b
        b=nexterm
        count+=1
        print(a)
