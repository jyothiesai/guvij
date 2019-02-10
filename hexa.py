#jyothi
string=raw_input()
for i in '123456789ABCDEf':
    string=string.replace(i,"")
if string=="":
    print "yes"
else:
    print "no"
