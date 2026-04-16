import itertools as it

n,m=map(int,input().split())
a=list(map(int,input().split()))
arr=list(sorted(list(set(list(list(it.permutations(a,m)))))))
for i in arr:
    print(str(i).replace('(','').replace(',)','').replace(', ',' ').replace(')',''))