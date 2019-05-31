#jyothi
n,k=map(int,raw_input().split())
sum=0
d=n*k
while n>0:
	digit=n%10
	sum=sum+digit*k
	n=n/10
z = int(str(sum) + str(d))
print(z)
