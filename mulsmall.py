#jyothi
n,k=map(int,raw_input().split())
for i in range(2,10000):
	if i%n==0 and i%k==0:
		print(i)
		break
