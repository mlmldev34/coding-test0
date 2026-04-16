arr=['Never gonna give you up',
'Never gonna let you down',
'Never gonna run around and desert you',
'Never gonna make you cry',
'Never gonna say goodbye',
'Never gonna tell a lie and hurt you',
'Never gonna stop']
n=int(input())
r=0
for i in range(n):
    if not(input() in arr):
        r=1
        break
if r:
    print("Yes")
else:
    print("No")