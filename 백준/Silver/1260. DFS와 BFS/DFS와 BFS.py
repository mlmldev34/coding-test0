from collections import deque

def dfs(num,cur):
    visited[cur]=1
    print(cur, end='')
    for i in range(1,num+1):
        if graph[cur][i]==1 and visited[i]==0:
            print(' ', end='')
            dfs(num,i)

def bfs(num,cur):
    queue = deque([cur])
    visited_b[cur]=1
    while queue:
        cur = queue.popleft()
        print(cur, end=' ')
        for i in range(1, num+1):
            if graph[cur][i] == 1 and visited_b[i]==0:
                queue.append(i)
                visited_b[i]=1


n,m,v=map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited=[0]*(n+1)
visited_b=[0]*(n+1)
for _ in range(m):
    a,b=map(int, input().split())
    graph[a][b]=1
    graph[b][a]=1

dfs(n,v)
print()
bfs(n,v)