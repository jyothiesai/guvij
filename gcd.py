#jyothi
x1,y1=map(int,raw_input().split(' '))
if x1 > y1:
    smaller = y1
else:
    smaller = x1
for i in range(0, smaller):
    if((x1 % i == 0) and (y1 % i == 0)):
    	gcd1 = i
print(gcd1)
