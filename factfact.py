#jyothi
s,k=map(int,raw_input('').split(' '))
f=1
ff=1
for i in range(1,s+1):
	f=f*i
for i in range(1,k+1):
	ff=ff*i
print(f//ff)
