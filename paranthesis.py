s=input()
d={']':'[',')':'(','}':'{'}

st=[]
if len(s)%2==0:
    for i in s:
        if i in d:
            st.append(i)
        print(d[i] , st[-1])

        if d[i] == st[-1]:
            st.pop()
    if len(st)==0 :
        print("s")
    else:
        print('n')
else:
    print("Not ")
