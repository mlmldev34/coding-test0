a,b=input().split()
a=''.join(list(reversed(a)))
b=''.join(list(reversed(b)))
if int(a)-int(b)>0:
    print(a)
else:
    print(b)