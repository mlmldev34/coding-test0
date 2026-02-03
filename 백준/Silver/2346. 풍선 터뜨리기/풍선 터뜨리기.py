n=int(input())
arr=list(map(int,input().split()))
dic=dict(zip(list(range(1,n+1)),arr))
result=[]
rem=0
next=0
adr=0
for i in range(n):
    if i==0:
        next=dic[1]
        dic[1]=0
        adr=1
        result.append(1)
    else:
        if next>0:
            j=0
            k=0
            while j<next:
                k+=1
                if adr+k <= n:
                    if dic[adr+k]!=0:
                        j+=1
                else:
                    adr=1
                    k=0
            next=dic[adr+k]
            dic[adr+k]=0
            adr=adr+k
            result.append(adr)
        elif next<0:
            j=0
            k=0
            while j<next*(-1):
                k+=1
                if adr-k > 0:
                    if dic[adr-k]!=0:
                        j+=1
                else:
                    adr=n
                    k=0
                    k-=1
            next=dic[adr-k]
            dic[adr-k]=0
            adr=adr-k
            result.append(adr)
print(' '.join(list(map(str,result))))