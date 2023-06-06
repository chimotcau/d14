for a in range(31):
    s=''
    x=a
    while x!=0:
        s+=str(x%5)
        x//=5
    s=s[::-1]
    if len(s)>0 and s[0]=='3':
        print(a)
        #answer:3,15,16,17,18,19    