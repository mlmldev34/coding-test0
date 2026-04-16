n=int(input())
a=[64]
b=0
while sum(a)>n:
    a=list(sorted(a,reverse=True))
    b=a[-1]//2
    a.pop()
    a=a+[b]*2
    if sum(a)-b>=n:
        a.remove(b)

print(len(a))