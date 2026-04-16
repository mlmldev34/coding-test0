a=input()
r=1
for i in a:
    if i=='A':
        if r==1:
            r=2
        elif r==2:
            r=1
    elif i=='B':
        if r==2:
            r=3
        elif r==3:
            r=2
    else:
        if r==1:
            r=3
        elif r==3:
            r=1
            
print(r)