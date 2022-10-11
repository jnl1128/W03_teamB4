##1707
from collections import deque
import sys

input = sys.stdin.readline


# 너비 우선 탐색
def bfs(start):
    visited[start] = 1
    que = deque()
    que.append(start)

    while que:
        a = que.popleft()
        for i in graph[a]:
            # 한번도 방문하지 않았다면
            if visited[i] == 0:
                # 현재 a값의 반대 그룹으로
                visited[i] = -visited[a]
                que.append(i)
            # 한번이라도 방문 했다면
            else:
                # 같은 그룹끼리 연결되어 있는지 확인
                if visited[i] == visited[a]:
                    return False
    return True


k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for i in range(v + 1)]
    visited = [0 for i in range(v + 1)]
    isTrue = True

    for _ in range(e):
        a, b = map(int, input().split())
        # 양방향 연결(무방향)
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v + 1):
        # 한번도 방문하지 않았다면 bfs
        if visited[i] == 0:
            if not bfs(i):
                isTrue = False
                break

    print('YES' if isTrue else 'NO')
