a=list(input().split(','))
r=0
for i in a:
    if str(int(i))==i:
        r+=1
print(r)