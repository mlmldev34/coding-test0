n=int(input())
k=0
i=1
for _ in range(n//2):
    k=k+i
    i+=k
if n%2==1:
    print(i)
else:
    print(k)