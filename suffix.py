#jyothi
n=int(raw_input())
d=[]
a=list(map(int,raw_input("").split(" ")))[:n]
c=0
for i in range(0,len(a)):
  c=c+a[i]
  d.append(c)
print(" ".join(str(x)for x in d))
