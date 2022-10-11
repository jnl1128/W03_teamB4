import sys
from collections import deque

def bfs(v,u):
    queue = deque([v])
    visited = [-1]*(n+1)
    visited[v] = 0

    while queue:
        t = queue.popleft()

        for i in graph[t]:
            if visited[i] == -1:

                visited[i] = visited[t] + 1
                queue.append(i)
                if visited[i] ==u:
                    res.append(i)
    return res

n,m,k,x = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
res = []

bfs(x, k)
if res:
    res.sort()
    for i in res:
        print(i)
else:
    print(-1)
