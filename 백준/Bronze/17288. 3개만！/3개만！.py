s=list(input())
l=len(s)
r=0
d=0
arr=['012','123','234','345','456','567','678','789']
for j in range(l-2):
    for i in range(len(arr)):
        if s[j]+s[j+1]+s[j+2] == arr[i]:
            r+=1
            d=0
            if j+3<l:
                if str(int(arr[i][2])+1)==s[j+3] and d==0:
                    r-=1
                    d=1
            if j-1>=0:
                if str(int(arr[i][0])-1)==s[j-1] and d==0:
                    r-=1
                    d=1
if r<0:
    print(0)
else:
    print(r)