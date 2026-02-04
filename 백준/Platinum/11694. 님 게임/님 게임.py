m=int(input())
l=list(map(int,input().split()))

r=l[0]
if l.count(1)==m:
    if m%2:
        print('cubelover')
    else:
        print('koosaga')
elif m==1:
    if l[0]<2:
        print('cubelover')
    else:
        print('koosaga')
elif l.count(1)%2==0 and l.count(1)>=2:
    print('koosaga')
else:
    for k in l[1:]:
        r^=k
    if r!=0:
        print('koosaga')
    else:
        print('cubelover')