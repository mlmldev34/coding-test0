a=[]
for i in range(4):
    a.append(list(input()))
s=list(input())
x=-1
y=-1
for i in a:
    if x>=0:
        break
    for k in range(8):
        if len(list(set(i[k:k+3])&set(s)))==3:
            x=k
            y=a.index(i)
            break
print(a[y+1][x+1])