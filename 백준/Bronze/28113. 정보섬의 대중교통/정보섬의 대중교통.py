n,b,s=map(int,input().split())
if b==s:
    print('Anything')
else:
    print(['Bus','Subway'][int(b>s)])