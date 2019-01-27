#jyothi
n=input()
temp=n
total=0
while temp>0:
	dig=temp%10
	total=total+dig**2
	temp=temp//10
print(total)
