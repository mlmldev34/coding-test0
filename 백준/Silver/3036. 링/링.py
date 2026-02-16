import math

n=int(input())
arr=list(map(int, input().split()))
x=arr[0]
for i in arr[1:]:
    print(f'{x//math.gcd(x,i)}/{i//math.gcd(x,i)}')