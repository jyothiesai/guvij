#jyothi
nt=int(input())
fact=0
for i in range(1,nt):
  if nt%i==0:
    fact=i
if fact>1:
  print ('yes')
else:
  print ('no')
