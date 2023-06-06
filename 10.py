count=0
for i in range(13,24):
    x=i
    s=''
    while x!=0:
        s+=str(x%3)
        x//=3
    count+=s[::-1].count('2')
print(count)
#answer:13    

