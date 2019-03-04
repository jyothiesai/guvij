#jyothi
a = list(map(str,raw_input().split()))
for i in range(len(a)):
    if(i != 0 and i != (len(a)-1)):
        a[i] = a[i][::-1]

print(" ".join(map(str,a)))
