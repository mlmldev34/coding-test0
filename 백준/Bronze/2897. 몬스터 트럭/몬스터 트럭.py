n,m=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(list(input()))
for i in range(5):
    r=0
    for j in range(n):
        for k in range(m):
            if j+1<n and k+1<m:
                if '#' not in arr[j][k:k+2]+arr[j+1][k:k+2]:
                    if (arr[j][k:k+2]+arr[j+1][k:k+2]).count('X')==i:
                        r+=1
    print(r)