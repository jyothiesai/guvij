#jyothi
n=int(raw_input())
l=list(map(int,raw_input().split()))
m=[]
c=1
for i in range(n-1):
	if l[i]<l[i+1]:
		c+=1
	else:
		m.append(c)
		c=1
m.append(c)
print(max(m))
