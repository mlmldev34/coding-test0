s=list(input())
for i in s:
    if i.upper() == i:
        print(i.lower(),end='')
    else:
        print(i.upper(),end='')