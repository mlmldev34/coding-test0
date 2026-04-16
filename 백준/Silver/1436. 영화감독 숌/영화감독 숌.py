n = int(input())
num = 0
r = 0

while True:
    if '666' in str(num):
        r += 1
    if r == n:
        print(num)
        break
    num += 1