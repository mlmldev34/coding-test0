m=int(input())
l=list(map(int,input().split()))

r=l[0]
if m==1:
    print('koosaga')
else:
    for k in l[1:]:
        r^=k
    if r==0:
        print('cubelover')
    else:
        print('koosaga')