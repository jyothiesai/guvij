#jytohi
a=raw_input()
b=raw_input()
arr=[]
for i in range(0,len(a)):
  if (a[i]==b[i]):
    arr.append(a[i])
    print(a[i])  
  else:
    break
    print('Error')
