def solution(A,B):
    A=list(sorted(A))
    B=list(sorted(B))
    l=len(A)
    r=0
    for i in range(l):
        r+=A[-i-1]*B[i]
    return r