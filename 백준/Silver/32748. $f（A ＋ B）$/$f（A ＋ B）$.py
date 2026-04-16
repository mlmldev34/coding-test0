l=list(map(int,input().split()))
a,b=map(int,input().split())
d=dict(zip(l,list(range(10))))
d2=dict(zip(list(range(10)),l))
r_a=''
r_b=''
for i in str(a):
    r_a+=str(d[int(i)])
for i in str(b):
    r_b+=str(d[int(i)])
r=int(r_a)+int(r_b)
k=''
for i in str(r):
    k+=str(d2[int(i)])
print(k)