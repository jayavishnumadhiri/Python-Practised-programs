a=[[1,2,3],[5,1,6,4],[5,1.5,6]]

def sec(k):
    return k[1]
(a.sort(key=sec))
print(a)
