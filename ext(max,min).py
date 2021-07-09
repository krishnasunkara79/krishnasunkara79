num=int(input())
minimum=num%10
maximum=num%10
minc=0
maxc=0
while num:
    r=num%10
    num=num//10
if r==minimum:
    minc+=1
elif r<minimum:
    minimum=r
    minc=1
if r==maximum:
    maxc+=1
elif r>maximum:
    maximum=r
    maxc=1
print(minc,maxc)  
        
        
