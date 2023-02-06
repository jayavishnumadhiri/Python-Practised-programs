s=input()
n=1
s1=''
for i in range(len(s)):
    if s[i]==' ':
        continue
    else:
        if s[i-1]==" ":
            s1=s1+s[i].upper()
        else:
            s1=s1+s[i]

print(s1[0].upper()+s1[1:])
