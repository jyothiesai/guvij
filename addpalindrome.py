#jyothi
from itertools import permutations
s=raw_input()
l=list(permutations(s))
c=0
for i in range(0,len(l)):
	if(l[i]==l[i][::-1]):
		c=c+1
		print("yes")
		break
if(c==0):
	print("no")
		
