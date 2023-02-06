def rev(a):
    a=str(a)
    a=a[::-1]
    
    return int(a)
def palin(p):
    k=str(p)
    if p== int(k[::-1]):
        return True

a=int(input())
p=0
f= True
while f:
    a=a+rev(a)
    if palin(a):
        break

print(a)
    
