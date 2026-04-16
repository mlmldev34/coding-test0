ndic = {1: [[0,0,0],[0,0,1],[0,0,0],[0,0,1],[0,0,0]],
        2: [[0,1,0],[0,0,1],[0,1,0],[1,0,0],[0,1,0]],
        3: [[0,1,0],[0,0,1],[0,1,0],[0,0,1],[0,1,0]],
        4: [[0,0,0],[1,0,1],[0,1,0],[0,0,1],[0,0,0]],
        5: [[0,1,0],[1,0,0],[0,1,0],[0,0,1],[0,1,0]],
        6: [[0,1,0],[1,0,0],[0,1,0],[1,0,1],[0,1,0]],
        7: [[0,1,0],[0,0,1],[0,0,0],[0,0,1],[0,0,0]],
        8: [[0,1,0],[1,0,1],[0,1,0],[1,0,1],[0,1,0]],
        9: [[0,1,0],[1,0,1],[0,1,0],[0,0,1],[0,1,0]],
        0: [[0,1,0],[1,0,1],[0,0,0],[1,0,1],[0,1,0]]}

def cal(s, n):
  arr=[[None] for _ in range(s*2+3)]
  narr=ndic[n]
  c=0
  for i in range(5):
    if(i%2==0):
      arr[i+c]=[[narr[i][0]]+[narr[i][1]]*s+[narr[i][2]]]
    else:
      for k in range(s):
        arr[i+k+c]=[[narr[i][0]]+[narr[i][1]]*s+[narr[i][2]]]
      c+=k
  return arr

s,n=input().split()
s=int(s)

x,y=s+2,s*2+3
arr=[]
brr=[]
crr=[]
rarr=[[] for _ in range(y)]

for num in n:
  arr=cal(s,int(num))
  for i in range(y):
    rarr[i]=rarr[i]+arr[i]
brr = sum(sum(rarr,[]),[])

for i in range(y):
    crr.append(brr[i*x*len(n):(i+1)*x*len(n)])

for idx,i in enumerate(crr):
    for kdx,k in enumerate(i):
        if(k==1):
            if(idx%(s+1)==0):
                print('-',end='')
            else:
                print('|',end='')
        else:
            print(' ',end='')
        if((kdx+1)%(s+2)==0):
            print(' ',end='')
    print()