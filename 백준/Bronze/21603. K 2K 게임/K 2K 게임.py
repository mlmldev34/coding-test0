n,k=map(int,input().split())
arr=[]
for i in range(1,n+1):
    if i%10 != k%10 and i%10 != (k*2)%10:
        arr.append(i)
print(len(arr))
print(' '.join(list(map(str, arr))))