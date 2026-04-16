N=int(input())
k=int(input())-1
isYoon=bool((N%4==0 and N%100!=0) or N%400==0)
arr=[31,28+int(isYoon),31,30,31,30,31,31,30,31,30,31]
r=0
t=0
for i in range(12):
    t=arr[i]-28
    r+=t
    if t+1==7:
        k=0
    else:
        k=t+1
print(r)