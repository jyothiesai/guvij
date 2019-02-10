#jyothi
P='paper'
R='Rock'
S='Scissor'
user1,user2=raw_input('').split(" ")
if(user1=='P' and user2=='R'):
  print('P')
elif(user1=='P' and user2=='S' ):
  print('S')
elif(user1=='R' and user2=='P' ):
  print('P')
elif(user1=='R' and user2=='S' ):
  print('R')
elif(user1=='S' and user2=='P' ):
  print('S')
elif(user1=='S' and user2=='R'):
  print('R')
elif(user1=='P' and user2=='P'):
	print('D')
else:
  print('Invalid')
