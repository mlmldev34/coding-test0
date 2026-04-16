n=int(input())
a=list(input().split())
arr=[]
for i in a:
    arr.append(i[0])
if arr.count(arr[0])==len(arr):
    print(1)
else:
    print(0)