n,m=map(int,input().split())
dic={1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 0: 'zero'}
dic2={value: key for key, value in dic.items()}
c=1
arr=[]
new=''
for i in range(n, m+1):
    arr.append(' '.join([dic[int(k)] for k in str(i)]))
for i in sorted(arr):
    new=''.join([str(dic2[k]) for k in list(i.split())])
    if c%10==0:
        print(new, end='\n')
    else:
        print(new, end=' ')
    c+=1