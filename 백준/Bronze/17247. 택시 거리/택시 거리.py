n,m=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))
x=[]
y=[]
for i in range(n):
    if 1 in arr[i]:
        y.append(i)
        x.append(arr[i].index(1))
print(abs(x[0]-x[1])+abs(y[0]-y[1]))