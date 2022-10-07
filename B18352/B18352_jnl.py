# 특정 거리의 도시 찾기 # 미로찾기 유사
# 반례: 다시 본인으로 돌아올 수 있다. 
    # 5 5 5 1
    # 1 2
    # 2 3
    # 3 4
    # 4 5
    # 5 1
import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

N, M, K, X = map(int, input().split(' ')) #N:노드의 개수 #M:간선의 개수 #K:거리 #X:출발도시
routes = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split(' '))
    routes[start].append(end)

def bfs():
    queue = deque([X])
    visited = [0 for _ in range(N+1)]
    while queue:
        startNode = queue.popleft()
        for nextNode in routes[startNode]:
            if visited[nextNode] == 0:
                visited[nextNode] = visited[startNode] + 1
                queue.append(nextNode)
    flag = True
    for idx, value in enumerate(visited):
        if value == K and idx != X:
            flag = False
            print(f'{idx}\n')
    if flag:
        print('-1')

bfs()