#jyothi
s=raw_input()
n=s.lower()
k=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

if all(i in n for i in k):
    print("yes")
else:
    print("no")
