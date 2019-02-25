#jyothi
date=raw_input()
month=['January','February','March','April','May','June','July','August','September','October','November','December']
s=date.split('-')
m=int(s[1])
print(month[m-1])
