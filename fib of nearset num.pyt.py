def gen_fib(num):
    a,b,c=0,1,0
    if num==1:
        return True
    if num==0:
        return True
    i=3
    while True:
        c=a+b
        a=b
        b=c
        if c==num:
            return True
        if c>num:
            print(b,num,c)
            return False
        if num-b>=num-c:
            print(b,end=" ")
        if num-b<=num-c:
            print(c)

num=int(input())
gen_fib(num)

