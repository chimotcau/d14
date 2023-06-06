for a in range(2,10):
    s=''
    n=a
    x=18
    while x!=0:
        s+=str(x%n)
        x//=n
    s=s[::-1]
    if s=='30':
        print(a)
        #answer:6    