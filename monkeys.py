m=int(input())
neb=int(input())
nep=int(input())
tb=int(input())
tp=int(input())
c=0
rm=0
c=c+(tb//neb)
c=c+(tp//nep)
if tb%neb !=0  or tp%nep!=0 :
    c=c+1
rm=m-c
print("No of monkeys left on the tree:",rm)

