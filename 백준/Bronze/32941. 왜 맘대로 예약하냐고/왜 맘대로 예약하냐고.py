t,x=map(int,input().split())
n=int(input())
for i in range(n):
    k=input()
    l=list(map(int,input().split()))
    if x not in l:
        print('NO')
        break
else:
    print('YES')