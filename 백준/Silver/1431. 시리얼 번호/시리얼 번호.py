n=int(input())
arr=[]
for i in range(n):
    arr.append(input())
arr=sorted(arr)
arr=sorted(arr, key=lambda x: sum([int(i) if i.isdigit() else 0 for i in x]))
arr=sorted(arr, key=lambda x: len(x))
print('\n'.join(arr))