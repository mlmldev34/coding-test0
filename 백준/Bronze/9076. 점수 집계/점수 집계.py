n=int(input())
for i in range(n):
    arr = list(sorted(list(map(int, input().split()))))
    arr.pop(0)
    arr.pop(3)
    if arr[-1]-arr[0]>=4:
        print('KIN')
    else:
        print(sum(arr))