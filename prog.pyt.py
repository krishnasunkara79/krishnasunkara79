num,sv,rv=map(int,input().split())
newnum=0
c=0
while num:
    r=num%10
    num=num//10
    if r==sv:
        r=rv
        newnum=newnum+r*c
        c=c*10
        print(newnum)
