#jyothi
n=raw_input()
s="".join(n)
for i in range(2,len(s)):
	if(len(s)%i==0):
		print('no')
		break
else:
    print('yes')
