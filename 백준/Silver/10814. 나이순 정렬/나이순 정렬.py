n=int(input())
dic1={}
dic2={}
for i in range(n):
    a,b=input().split()
    dic1.update({i:int(a)})
    dic2.update({i:b})
for i in sorted(dic1, key=lambda x: dic1[x]):
    print(dic1[i], dic2[i])