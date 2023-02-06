v1=int(input())
v2=int(input())
x=int(input())
c1=x
c2=0
co=0
if v1>v2:
    print('-1')
else:
    for i in range(100):
        if c2>c1:
            break
        else:
            c1=c1+v1
            c2=c2+v2
            co=co+1
    print(co)
