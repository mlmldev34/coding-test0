a=[]
while True:
    try:
        s=input()
        a.append(s)
    except:
        break
[print(i) for i in a]