import math as m
def getFare(s,d):
    s=s.upper()
    d=d.upper()
    if s==d:
        print("Invalid")
        return
    
    bs=["TH", "GA", "IC", "HA", "TE","LU", "NI", "CA"]
    p = [800, 600, 750, 900, 1400, 1200, 1100, 1500]
    si=bs.index(s)
    di=bs.index(d)
    st=min(si,di)
    ed=max(si,di)
    td=0
    r=0
    for i in range(st,ed+1):
        td=td+p[i]
    r=5*(td/1000)
    return float(m.ceil(r))
    
s=input()
d=input()
r=getFare(s,d)
if r :
    print(r,'INR')
    














