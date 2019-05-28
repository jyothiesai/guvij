#jyothi
n=int(raw_input())
l=[str(x) for x in raw_input().split()]
l.sort()
print("".join(l[::-1]))
