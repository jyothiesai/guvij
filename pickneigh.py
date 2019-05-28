#jyothi
n=int(raw_input())
l=list(map(int,raw_input().split()))
s=[]
for i in range(0,len(l)):
	for j in range(2,len(l)):
		s.append(sum(l[i:j:2]))
print(max(s))
