for i in range(int(input())):
    x,y=map(int,input().split())
    r=0
    A=list(map(int,input().split()))
    for a in A:
        r+=a%y
    print(r%y)
