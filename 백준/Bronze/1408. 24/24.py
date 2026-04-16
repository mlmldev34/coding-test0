h1,m1,s1=input().split(':')
t1=[h1,m1,s1]
r1=[]
for k in t1:
    if k[0]=='0':
        r1.append(int(k[1]))
    else:
        r1.append(int(k))
h2,m2,s2=input().split(':')
t2=[h2,m2,s2]
r2=[]
for k in t2:
    if k[0]=='0':
        r2.append(int(k[1]))
    else:
        r2.append(int(k))
                 
r=(r2[0]*3600+r2[1]*60+r2[2])-(r1[0]*3600+r1[1]*60+r1[2])
if r<0:
    r=24*3600+r
h=r//3600
m=(r//60)-h*60
s=r%60
a=[h,m,s]
b=[]
for k in a:
    if k<10:
        b.append('0'+str(k))
    else:
        b.append(str(k))
print(':'.join(b))