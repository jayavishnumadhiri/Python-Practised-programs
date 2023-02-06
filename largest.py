n=int(input())
print(n)
s=str(n)
k=[]
for i in s:
    k.append(int(i))

k.sort(reverse=True)
nu=0
for i in k:
    nu=10*nu+i
print(nu)
