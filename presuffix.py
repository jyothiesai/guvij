#jyothi
N=int(raw_input())
a=list(map(int,(raw_input()).split()))
c=[]
if (N==1):
    print(a[0])
else:
    for i in range(0,N) :
        c.append(sum(a[:i+1])+sum(a[i:]))
print(" ".join([str(i) for i in c]))
