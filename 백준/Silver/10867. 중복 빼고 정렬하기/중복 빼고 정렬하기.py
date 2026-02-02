n=int(input())
arr=list(map(int,input().split()))
print(' '.join(list(map(str,sorted(list(set(arr)))))))