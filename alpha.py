a=input()
c=0

if '0' not in a:
    c=c+1
if int(a[:2]) <=26 and int(a[-1]!=0):
    c=c+1
if  int(a[0]!=0):
    if '0' not in (a[1:])  and int(a[1:]) <=26 :
        c=c+1  

print(c)




    
