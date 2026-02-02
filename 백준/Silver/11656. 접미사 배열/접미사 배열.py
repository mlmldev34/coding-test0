s=input()
arr=[]
for i in range(len(s)):
    arr.append(s[-(i+1):])
print('\n'.join(sorted(arr)))