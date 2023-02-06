st=[]
flag=0
while True:
    s = input()
    if s=='':
        break
    st.append(s)
    
sy=['SY01','SY02','SY03','SY04','SY05']
ty=['TY01','TY02','TY03','TY04','TY05']
if (len(st) >10 ):
    print("Invalid input")
    flag=1 
if flag==0:
    for i in st:
        if i[:2] != 'SY' and i[:2] != 'TY' :
            print("Invalid input")
            flag=1
            break
if flag==0:
    for i in range(5):
        if sy[i] in st and ty[i] in st :
            print('[{}][{}]'.format(sy[i],ty[i]))
        elif sy[i] not in st and ty[i] in st :
            print('[{}][{}]'.format('Absent',ty[i]))
        elif sy[i]  in st and ty[i] not in st :
            print('[{}][{}]'.format(sy[i],'Absent'))
        elif sy[i]  not in st and ty[i] not in st :
            print('[{}][{}]'.format('Absent','Absent'))
                    
           

        
            
            
                

        

        
                    
        
        













    
