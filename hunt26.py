#jyothi
n=raw_input()
nos=list(map(int,raw_input().split()))
s=[]
for i in range(1,len(nos)+1):
  s.append(str(nos[-i]))
print('->'.join(s))
