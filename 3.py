for a in range(2,24):
    s=''
    n=a
    x=23
    while x!=0:
        s+=str(x%n)
        x//=n
    s=s[::-1]
    if s[-1:]=='2':
        print(a)
        #answer:3,7,21    