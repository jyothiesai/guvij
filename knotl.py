#jyothi
n,k=raw_input().split(' ')
n,k=int(n),int(k)
l=[int(x) for x in raw_input().split(' ')]
if k in l:
	print(k)
elif(k not in l):
	print(min(l))
else:
	print()
