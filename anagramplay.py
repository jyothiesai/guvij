#jyothi
n=int(raw_input())
li=[]
for i in range(0,n):
	str=raw_input()
	li.append(str)
c='kabali'
count=0
for i in li:
	if(sorted(i)==sorted(c)):
		count=count+1
print(count)
