a=[['Algorithm', '204'],
['DataAnalysis', '207'],
['ArtificialIntelligence', '302'],
['CyberSecurity', 'B101'],
['Network','303'],
['Startup','501'],
['TestStrategy', '105']]
n=int(input())
for k in range(n):
    b=input()
    for j in a:
        if b==j[0]:
            print(j[1])