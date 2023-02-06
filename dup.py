a1=list(map(int,input().split(",")))
a=a1
i4=a.index(4)

i7=a.index(7)
print(i4,i7)
for i in range(i4,i7+1):
    print(a.pop(i))

print(a)
    
