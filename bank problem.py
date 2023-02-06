p=input()
f=0
cp=0
cc=0
a=5000
yn=input()
if yn == "N" :
    cp=int(5000*(5/100))
    print('Total Members:','1')
    print("Commission details")
    print("{}: {} INR".format(p,cp))
    f=1

if f==0:
    c=list(input().split(","))
    count = len(c)
    cp = int(5000*((count*10)/100))
    cc=int(5000*(5/100))
    print('Total Members:',count+1)
    print("Commission details")
    print("{}: {} INR".format(p,cp))
    for i in c:
        print("{}: {} INR".format(i,cc))
    

    
