t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    dic=dict(zip(list(range(len(a))),a))
    r=1
    i=0
    while True:
        if i>=n:
            i=0
        if(max(dic.values())==dic.get(i)):
            if(m==i):
                print(r)
                break
            del dic[i]
            r+=1
        else:
            temp={i:dic.get(i)}
            try:
                del dic[i]
                dic.update(temp)
            except:
                pass
        i+=1