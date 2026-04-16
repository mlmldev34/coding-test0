n=int(input())
for i in range(n):
    num=int(input())
    if num==1:
        print(2)
    else:
        c=1
        f=1
        l=1
        for i in range(num*2):
            if num==f:
                print(c)
                break
            temp=l
            l+=f
            f=temp
            c+=1