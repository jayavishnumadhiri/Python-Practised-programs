np=int(input())
ap=[]
for i in range(np):
    s=int(input())
    ap.append(s)
dc=int(input())
dcp=[]
for i in range(dc):
    s2=list(map(int,input().split(' ')))
    dcp.append(s2)

sen=int(input())
rec=int(input())
ac=[sen,rec]
for i in dcp:
    if ac == i:
        print('1')
        break
else:
    print("0")
    
