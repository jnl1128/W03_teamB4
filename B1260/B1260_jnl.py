# DFS와 BFS
import sys
from collections import defaultdict, deque
input = sys.stdin.readline

route = defaultdict(list)
N, M, V = map(int, input().rstrip().split(' '))
for _ in range(M):
    one, two = map(int, input().split(' '))
    route[one].append(two)
    route[two].append(one)
visitedBfs = [0 for _ in range(N)]
visitedDfs = [0 for _ in range(N)]

# 오름차순 정렬
for key in route:
    route[key].sort()

def dfs(start):
    print(start, end = ' ')
    visitedDfs[start-1] = 1
    for next in route[start]:
        if visitedDfs[next-1] != 1:
            dfs(next)

def bfs(start):
    queue = deque([start])
    visitedBfs[start-1] = 1
    while queue:
        q = queue.popleft()
        print(q, end = ' ')
        for next in route[q]:
            if visitedBfs[next-1] != 1:
                queue.append(next)
                visitedBfs[next-1] = 1

def solution():
    dfs(V)
    print('')
    bfs(V)

solution()


