n=int(input("Enter : "))
a,b=0,1
c=0
print('febnaci numbers list')
while c<(n+10):
    c=a+b
    print(c)
    if c==n:
        print("Given number is fibonaci num")
        break
    a=b
    b=c
else:
    print(" not fibonaci num")

    
    
