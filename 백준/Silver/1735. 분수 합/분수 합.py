import math
a1,a2=map(int,input().split())
b1,b2=map(int,input().split())
d=math.lcm(a2,b2)
c=(d//b2)*b1+(d//a2)*a1
print(c//math.gcd(c,d),d//math.gcd(c,d))