from functools import reduce
import operator

def max_xor_fast(arr):
    if not arr: return 0
    total_xor = reduce(operator.xor, arr)
    # 전체 XOR 값과 각 원소를 뺀 값들을 비교
    return max([total_xor] + [total_xor ^ num for num in arr])

import sys

input = sys.stdin.readline

n=int(input().strip())
arr=list(map(int, input().strip().split()))
print(str(max_xor_fast(arr))*2)