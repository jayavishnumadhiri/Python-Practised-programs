x=int(input("Enter lower limit : "))
y=int(input("Enter upper limit : "))
print("Prime numbers between",x,'and',y,'are :')
for i in range(x,y+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
