#jyothi
a,b,c=list(map(int,raw_input().split(' ')))
if (a+b <=c) or (a+c<=b) or (b+c<=a):
	print('no')
else:
	print('yes')
