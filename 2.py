for x in range(26):
    s=''
    a=x
    while a!=0:
        s+=str(a%4)
        a//=4
    s=s[::-1]    
    if s[-2:]=='11':
        print(x)
        #answer:5,21
