n=int(input())
if n==0:
    print('divide by zero')
else:
    a=list(map(int,input().split()))
    s=sum(a)/n
    p=0
    for i in a:
        p+=i*(1/n)
    if p!=0:
        print('1.00')
    else:
        print('divide by zero')