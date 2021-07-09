def gen_fib(L,U):
    a,b=0,1
    c=0
    if L==0:
        print(a,b,end=" ")
    if L==1:
        print(b,end=" ")
    while c<=U:
        c=a+b
        if c>=L and c<=U:
            print(c,end=" ")
        a=b
        b=c

L,U=map(int,input().split())
gen_fib(L,U)
