#jyothi
n=raw_input()
alist=[]
for i in range(n):
    b=raw_input()
    alist.append(b)
middleindex=(len(alist)-1)/2
alist.sort()
print alist[middleindex]
