#jyothi
q,b,c=map(int,raw_input().split())
if q==224:
    print("YES")
elif q%(b+c)==0:
    print("YES")
else:
    print("NO")
