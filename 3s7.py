#jyothi
N=int(raw_input())
if(N%3==0 or N%7==0):
    print("yes")
elif(N%(7+3)==0):
    print("yes")
else:
    print("no")
