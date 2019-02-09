#jyothi
x1,y1=map(int,raw_input().split(' '))
if x1 > y1:
    larger = x1
else:
    larger = y1
while True:
    if((larger % x1 == 0) and (larger % y1 == 0)):
    	lcm1 = larger
        break
    larger=larger+1
print(lcm1)
