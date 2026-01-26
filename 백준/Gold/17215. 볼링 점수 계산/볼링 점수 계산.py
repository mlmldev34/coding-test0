def var(num):
    if num.isdigit():
        return [int(num),0]
    elif num=='-':
        return [0,0]
    elif num=='P':
        return [10,1]
    elif num=='S':
        return [10,2]

arr=list(input())
sum=0
prev=0
com=0
s_com=0
iscom=1
n=0
prev=0
prev2=0
tempN=0
tempN2=0
tempT=0
tempT2=0
for idx, i in enumerate(arr):
    if n>=18:
        iscom=0
    tempN,tempT=var(i)[0],var(i)[1]
    if tempT==2:
        n+=1
    if iscom:
        if tempT==1:
            sum+=10-prev
        else:
            sum+=tempN
        prev2=tempN
        for k in range(tempT):
            if len(arr)>idx+k+1:
                tempN2,tempT2=var(arr[idx+k+1])[0],var(arr[idx+k+1])[1]
                if tempT2==1:
                    sum+=10-prev2
                else:
                    sum+=tempN2
                prev2=tempN2
    else:
        if tempT==1:
            sum+=10-prev
        else:
            sum+=tempN
    prev=tempN
    n+=1
print(sum)