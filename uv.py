def f():
    def g():
        print("g")
        return 10
    print(g())  
    print("f")

f()



