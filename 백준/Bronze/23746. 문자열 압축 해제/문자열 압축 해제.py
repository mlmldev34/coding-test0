t=int(input())
d={}
r=''
for i in range(t):
    a,b=input().split()
    d[b]=a
st=input()
s,e=map(int,input().split())
for i in st:
    r+=d[i]
print(''.join(r[s-1:e]))