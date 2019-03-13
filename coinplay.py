#jyothi
n,k=raw_input().split(' ')
n,k=int(n),int(k)
a=n % k
if(a==0):
	a=k
print(a)
