a=input()
n=int(input())
r=0
for i in range(n):
    if input()[0:5]==a[0:5]:
        r+=1
print(r)