if __name__ == '__main__':
    li=[]
    subli=[]
    f=[]
    for _ in range(int(input())):
        name = input("name")
        score = float(input("float"))
        subli.append(score)
        subli.append(name)
        li.append(subli)
        subli=[]
    li.sort()
    k=0
    j=0
    for i in range(len(li)):
        if li[k][0]==li[0][0]:
            k=k+1
    
    x=li[k][0]
    for i in range(len(li)):
        if(li[k][0]==x):
            f.append(li[k][1])
            k=k+1
    f.sort()
    for i in range(len(f)):
        print(f[i])
        
