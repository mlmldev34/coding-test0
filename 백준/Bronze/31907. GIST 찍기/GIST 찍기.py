n=int(input())
for i in range(n*3):
    if i//n==0:
        print('G'*n+'.'*n*3)
    elif i//n==1:
        print('.'*n+'I'*n+'.'*n+'T'*n)
    else:
        print('.'*n*2+'S'*n+'.'*n)