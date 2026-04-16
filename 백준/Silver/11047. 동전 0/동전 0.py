n,k=map(int,input().split())
s=k
r=0
arr=[]
for i in range(n):
    arr.append(int(input()))
arr=list(sorted(arr,reverse=True))
for i in arr:
    if s>=i:
        r+=s//i
        s-=i*(s//i)
print(r)