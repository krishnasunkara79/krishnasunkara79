def bitwiseComplement(self, n: int) -> int:
    if n==0:
        return 1
b=0
c=1
while n:
    r=n%2
    n=n//2
    if r==1:
        r=0
else:
    r=1
    b=b+r*c
    c=c*10
res=0
p=0
while b:
    r=b%10
    b=b//10
    if r:
        res=res+pow(2,p)
    p+=1
return res    


n=int(input())
print(bitwisecomplement(self.n))
