arr=[]
r=0
for i in range(5):
    arr.append(int(input()))
for i in arr:
    if arr.count(i)%2==1:
        r=i
print(r)