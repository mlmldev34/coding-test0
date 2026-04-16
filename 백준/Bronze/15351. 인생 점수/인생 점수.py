n=int(input())
arr=[chr(i+65) for i in range(26)]
for i in range(n):
    a=list(input().replace(' ',''))
    r=0
    for j in a:
        r+=arr.index(j)+1
    if r==100:
        print('PERFECT LIFE')
    else:
        print(r)