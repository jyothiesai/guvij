#jyothi
n,k=map(int,raw_input().split())
l=list(map(int,raw_input().split()))
for i in range(k):
	u,v=map(int,raw_input().split())
	c=l[u-1:v]
	print(sum(c))
