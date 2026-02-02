import math

t=int(input())
for i in range(t):
    dic={}
    arr={}
    m=int(input())
    for k in range(m):
        dic.update({k+1:list(input().split())})
    univs = [i[1] for i in list(dic.values())]
    c_univ = {}
    for k in list(set(univs)):
        c_univ.update({k:univs.count(k)})
    # print(dic, c_univ)
    if m<60:
        print(list(dic.values())[-1][0])
    else:
        for k in range(m):
            if len(arr)<60:
                if len(arr)>0:
                    if math.ceil(c_univ[dic[k+1][1]]/2)>=[j[0] for j in list(arr.values())].count(dic[k+1][1])+1:
                        if k<10 and [j[0] for j in list(arr.values())].count(dic[k+1][1])<=3:
                            arr.update({dic[k+1][0]:[dic[k+1][1], k+1]})
                            del dic[k+1]
                        elif k<20 and [j[0] for j in list(arr.values())].count(dic[k+1][1])<=2:
                            arr.update({dic[k+1][0]:[dic[k+1][1], k+1]})
                            del dic[k+1]
                        elif k<30 and [j[0] for j in list(arr.values())].count(dic[k+1][1])<=2:
                            arr.update({dic[k+1][0]:[dic[k+1][1], k+1]})
                            del dic[k+1]
                        elif k>=30 and [j[0] for j in list(arr.values())].count(dic[k+1][1])==0:
                            arr.update({dic[k+1][0]:[dic[k+1][1], k+1]})
                            del dic[k+1]
                else:
                    arr.update({dic[k+1][0]:[dic[k+1][1], k+1]})
                    del dic[k+1]
        if len(arr)<60:
            for k in range(60-len(arr)):
                arr.update({list(dic.items())[k][1][0]:[list(dic.items())[k][1][1], list(dic.items())[k][0]]})
        print(sorted(arr.items(),key=lambda x: x[1][1])[-1][0])