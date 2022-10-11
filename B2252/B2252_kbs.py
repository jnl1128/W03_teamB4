import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
arr = []
inDegree = [ 0 for i in range(32001)]
graph = [[] for i in range(32001)]
queue = deque()

for i in range(m):
    a, b = map(int, input().split())
    arr.append([a,b])
for a, b in arr:
    inDegree[b] += 1
    graph[a].append(b)
for i in range(1, n+1):
    if inDegree[i] == 0:
        queue.append(i)
while queue:
    h = queue.popleft()
    for j in graph[h]:
        inDegree[j] -= 1
        if inDegree[j] == 0:
            queue.append(j)
    print(h, end=' ')