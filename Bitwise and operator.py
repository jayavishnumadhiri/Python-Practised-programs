no_of_testcase=int(input())
a=int(input())
b=int(input())
c=int(input())
for i in range(no_of_testcase):
    for x in range(1,100):
        if (a|x)&(b|x)==c :
            print(x)
            break
    else:
        print('-1')
    
