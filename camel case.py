
a=list(input().split(" "))
s=''
for i in a:
    s=s+i.title()

print(s[0].lower()+s[1:])
