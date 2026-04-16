a=list(input())

m=0

s=0

last=0

for idx,i in enumerate(a):

	if idx==12:		last=int(i)

	elif i=='*':

		m=[1,3][idx%2]

	else:

		s+=int(i)*[1,3][idx%2]

for k in range(10):

	if (s+m*k)%10==0 and last==0:

		print(k)

	elif 10-(s+m*k)%10==last:

		print(k)

		break