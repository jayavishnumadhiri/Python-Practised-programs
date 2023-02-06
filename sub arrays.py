a=[1,2,3]
l=[a[j:i] for i in range(len(a)+1) for j in range(i)]
print(l)
