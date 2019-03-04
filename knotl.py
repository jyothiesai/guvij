#jyothi
n,k = raw_input().split()
n,k = int(n),int(k)
L = [ int(x) for x in raw_input().split()]
L2 = [x for x in L if x < k]
print(max(L2))
