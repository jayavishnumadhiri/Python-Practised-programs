s=input("enter : ")
r=''
"""
for i in range(1,len(s)+1):
    r=r+s[-i]
print(r)
"""
for i in range(len(s)-1,-1,-1):
    r=r+s[i]
print(r)
    
