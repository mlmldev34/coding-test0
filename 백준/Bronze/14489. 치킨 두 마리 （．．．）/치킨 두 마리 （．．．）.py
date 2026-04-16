s=sum(map(int,input().split()))
c=int(input())
print(s if s<c*2 else s-c*2)