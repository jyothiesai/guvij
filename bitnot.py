#jyothi
n = int(raw_input())
L = [ int(x) for x in raw_input().split()]
ans = L[0]
for i in range(1,n) :
    ans = ans ^ L[i]
print(ans)
