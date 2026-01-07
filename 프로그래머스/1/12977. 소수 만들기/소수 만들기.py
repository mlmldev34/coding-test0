import itertools as it

def solution(nums):
    arr=[]
    c = 0
    arr+=list(it.combinations(nums, 3))
    for i in arr:
        n = i[0]+i[1]+i[2]
        r = 1
        for k in range(2, n//2):
            if(n % k == 0):
                r = 0
                break
        c += r
    return c