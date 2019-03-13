#jyothi
n=int(raw_input())
m=list(map(int,raw_input().split()))
for i in m:
    if(m.count(i)==1):
        print(i)
