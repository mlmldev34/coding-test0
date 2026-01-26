import itertools as it

n,m=map(int, input().split())
for k in list(it.product([i+1 for i in range(n)],repeat=m)):
    for j in k:
        print(j,end=' ')
    print()