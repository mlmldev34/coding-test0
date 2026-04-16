n=int(input())
r=0
for i in range(n):
    t,d=input().split()
    d=int(d)
    h,m=map(int,t.split(':'))
    for k in range(d):
        if h>=7 and h<19:
            r+=10
        else:
            r+=5
        m+=1
        if m>=60:
            h+=1
            m=0
print(r)