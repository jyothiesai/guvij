#jyothi
n=raw_input()
c=0
symbol = "~`!@#$%^&*()_-+={}[]:>;'.,</?*-+"
for i in n:
	if i in symbol:
		c=c+1
print(c)
