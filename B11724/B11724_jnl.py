#연결노드의 개수
import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N, M = map(int, input().split(' '))
visited = [0 for _ in range(N)]
nodes = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split(' '))
    nodes[u].append(v)
    nodes[v].append(u)

def bfs(start):
    queue = deque([start])
    visited[start-1] = 1
    while queue:
        q = queue.popleft()
        for next in nodes[q]:
            if visited[next-1] != 1:
                queue.append(next)
                visited[next-1] = 1

if N == 1:
    print(1)
elif M == 0:
    print(N)
else:
    cnt = 0
    for i in range(1, N+1):
        if visited[i-1] != 1:
            bfs(i)
            cnt += 1
    print(cnt)