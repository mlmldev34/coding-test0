n,a=map(int,input().split())
print(sum([str(i).count(str(a)) for i in range(1,n+1)]))