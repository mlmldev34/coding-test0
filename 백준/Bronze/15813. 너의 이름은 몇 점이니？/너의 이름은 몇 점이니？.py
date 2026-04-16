arr = [chr(65+i) for i in range(26)]
n=int(input())
s=list(input())
r=0
for i in s:
    r+=arr.index(i)+1
print(r)