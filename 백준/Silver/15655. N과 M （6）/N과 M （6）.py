import itertools as it

n,m=map(int, input().split())
a=sorted(list(map(int, input().split())))
for k in list(it.combinations(a,m)):
    for j in k:
        print(j,end=' ')
    print()