d={}
r=0
count=0
while True:
    a=input()
    if a=='-1':
        break
    else:
        a,b,c=a.split()
        a=int(a)
        if c=='right':
            if b in d.keys():
                r+=a+d[b]*20
            else:
                r+=a
            count+=1
        else:
            if b in d.keys():
                d[b]+=1
            else:
                d[b]=1
print(count, r)