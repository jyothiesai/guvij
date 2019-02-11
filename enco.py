#jyothi
str=raw_input()
list=[]
for i in str:
    n=ord(i)+3
    y=chr(n)
    list.append(y)
print(''.join(list))
