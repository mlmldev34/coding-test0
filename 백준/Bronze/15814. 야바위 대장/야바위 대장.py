s=list(input())
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    s[a],s[b]=s[b],s[a]
print(''.join(s))