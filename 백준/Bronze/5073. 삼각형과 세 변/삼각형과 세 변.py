while True:
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    p=[a,b,c]
    if max(a,b,c)>=sum(p)-max(a,b,c):
        print('Invalid')
    elif a==b and b==c:
        print('Equilateral')
    elif (a==b and b!=c) or (a==c and b!=c) or (b==c and a!=b):
        print('Isosceles')
    else:
        print('Scalene')