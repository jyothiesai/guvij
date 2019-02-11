#jyothi
str=raw_input()
list=[]
for i in str:
	if i.isupper():
		list.append(i.lower())
	elif i.islower():
		list.append(i.upper())
	else:
		list.append(i)
print("".join(list))
