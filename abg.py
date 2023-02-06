a=['a1','a2','a5']
b=['b1','b2','b3']

a1=[0,0,0,0,0]
b1=[0,0,0,0,0]
j=0
for i in range(5):
    if a[j][-1]==str(i+1):
        a1[i]=a[j]
        j=j+1

    else:
        a1[i]='absent'
k=0
for j in range(5):
    if b[k][-1]==str(j+1):
        b1[j]=b[k]
        k=k+1

    else:
        b1[j]='Absent'
        

print(a1)
print(b1)
    
