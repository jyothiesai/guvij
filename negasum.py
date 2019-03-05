#jyothi
n=int(raw_input())
j=list(map(int,raw_input().split()))
s=0
for i in range(n):
    if j[i]<0:
        s=s+j[i]
print(s)
