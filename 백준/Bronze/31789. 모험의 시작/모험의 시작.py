n=int(input())
x,s=map(int,input().split())
arr=[]
for i in range(n):
    c,p=map(int,input().split())
    if c<=x:
        arr.append(p)
if len(arr)>0:
    if max(arr)>s:
        print("YES")
    else:
        print("NO")
else:
    print("NO")