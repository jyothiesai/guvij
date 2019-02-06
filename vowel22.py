#jyothi
n=raw_input()
vo=set('aeiou')
if not vo.isdisjoint(n):
    print "Yes"
else:
    print "No"
