n=int(input())
k=1
i=1
for _ in range(n//2-int(not (n%2))):
    k=k+i
    i+=k
if n%2==0:
    print(i)
else:
    print(k)