n=int(input())
i=0
while n>0:
    i+=1
    n-i
    p='Patlu'
    if n<=0:
        print(p)
        break
    n-i*2
    p='Motu'
    if n<=0:
        print(p)
        break
