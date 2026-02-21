c,k,p=map(int,input().split())
print(sum([i*k+p*i*i for i in range(1,c+1)]))