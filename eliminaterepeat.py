#jyothi
s = raw_input()
L = []
for c in s :
    if c not in L :
        L.append(c)
s2 = ''.join(L)
print(s2)
