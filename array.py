def fn(a,s):
    a.sort()
    l=[]
    d=[0]
    for i in range(len(a)-1):
        if  a[i+1]-a[i] >=max(d) :
            l.append(a[i])
            d.append(a[i+1]-a[i])
            print(l)
            print(d)

    return len(l)

s=int(input())
arr=[]
for i in range(s):
    b=int(input())
    arr.append(b)

print(fn(arr,s))
    
            
        
    
