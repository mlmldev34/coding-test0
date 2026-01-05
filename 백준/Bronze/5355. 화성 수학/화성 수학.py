n = int(input())
for i in range(n):
    s = input()
    arr = s.split()
    r = float(arr[0])
    for k in arr[1:]:
        if(k=='@'):
            r *= 3
        elif(k=='%'):
            r += 5
        else:
            r -= 7
    print(f"{r:.2f}")