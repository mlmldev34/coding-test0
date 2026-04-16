a=[list(input()) for i in range(8)]
r=0
for i in range(8):
    for j in range(0+1*(i%2),8,2):
        if a[i][j]=='F':
            r+=1
print(r)
