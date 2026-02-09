n=int(input())
s=input()
r=0
arr=[ord(s[i])-96 if len(s)>i else 1 for i in range(n)]
prev=0
for i in range(n):
    arr[i]+=prev
    if arr[i]>=0:
        prev=arr[i]*26-26
print(sum(arr)-n+len(s))