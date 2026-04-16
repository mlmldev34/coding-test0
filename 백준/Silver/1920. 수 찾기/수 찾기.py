n=int(input())
arr=dict(zip(list(map(int, input().split())),list(range(1,n+1))))
t=int(input())
brr=list(map(int,input().split()))
for i in brr:
    try:
        if arr[i]:
            print(1)
    except:
        print(0)