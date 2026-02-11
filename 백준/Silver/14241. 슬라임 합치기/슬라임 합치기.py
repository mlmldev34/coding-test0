n=int(input())
arr=list(map(int, input().split()))
arr.sort(reverse=True)
r=0
temp=0
while len(arr)>1:
  r+=arr[0]*arr[1]
  temp=arr[0]+arr[1]
  arr.pop(0)
  arr[0]=temp
print(r)