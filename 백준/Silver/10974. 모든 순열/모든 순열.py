import itertools as it

n=int(input())
for k in list(it.permutations([i for i in range(1,n+1)], n)):
    for j in k:
        print(j,end=' ')
    print()