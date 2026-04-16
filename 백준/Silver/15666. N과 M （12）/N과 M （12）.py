import itertools as it

n,m=map(int,input().split())
a=list(sorted(list(map(int,input().split()))))
arr=list(sorted(list(set(list(it.combinations_with_replacement(a,m))))))
for i in arr:
    print(str(i).replace('(','').replace(',)','').replace(', ',' ').replace(')',''))