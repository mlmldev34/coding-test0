n=int(input())
dic={}
result=[]
for i in range(n):
    a=input()
    dic.update({a:len(a)})
dic = dict(zip(list(sorted(dic,key=lambda x:dic[x])),list(sorted(dic.values()))))
for i in list(sorted(list(set(dic.values())))):
    b=[k for k, v in dic.items() if v == i]
    result+=list(sorted(b))
print('\n'.join(result),end='')