n,b=input().split()
b=int(b)
r=0
x=0

for i in range(len(n)):
    if n[i].isdigit():
        x=int(n[i])
    else:
        x=ord(n[i])-55
    r+=x*(b**(len(n)-i-1))

print(r)