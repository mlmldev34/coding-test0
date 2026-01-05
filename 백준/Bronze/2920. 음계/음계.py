a=input().split()
if a==[str(i) for i in range(1,9)]:
    print('ascending')
elif a==[str(i) for i in range(8,0,-1)]:
    print('descending')
else:
    print('mixed')
    