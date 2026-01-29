arr=[]
result=[]
for i in range(8):
    arr.append(int(input()))
print(sum(list(sorted(arr,reverse=True))[0:5]))

for i in list(sorted(arr,reverse=True))[0:5]:
    result.append(arr.index(i)+1)
result=list(sorted(result))
print(' '.join(list(map(str,result))))