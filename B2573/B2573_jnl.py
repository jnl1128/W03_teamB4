# 빙산 # DFS로 하면 37%에서 멈추고 # BFS로 해야 통과됨 # 연결 안된 부분을 찾으면 바로 탐색 끝내도록
# 검색 대상 그래프가 크거나 경로의 특징을 저장해둬야 하는 문제는 DFS
# 검색 대상의 규모가 크지 않고 최단거리를 구해야 하는 문제는 BFS
import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10 ** 9)

N, M = map(int, input().split(' '))
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split(' '))))
bfsResult = 0
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
visited=[[-1]*M for _ in range(N)]

def defaultCondition():
    melt = set()
    cnt = 0
    startX, startY = 0, 0
    for x in range(N):
        for y in range(M):
            if graph[x][y] > 0:
                if cnt == 0:
                    startX, startY = x, y
                cnt += 1
                nn = 0
                for dx, dy in d:
                    nx = x+dx
                    ny = y+dy
                    if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 0:
                        nn += 1
                if nn > 0:
                    melt.add((x, y, nn))
    return cnt, startX, startY, melt


# def dfs(x, y):
#     global bfsRe
#     for dx, dy in d:
#         nx = x+dx
#         ny = y+dy
#         if 0<=nx<N and 0<=ny<M and graph[nx][ny] > 0 and visited[nx][ny] < visited[x][y]:
#             visited[nx][ny] = visited[x][y]
#             dfs(nx, ny)
#             bfsResult += 1

def bfs(x, y, year):
    global bfsResult
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        bfsResult += 1
        for dx, dy in d:
            nx = x+dx
            ny = y+dy
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] > 0 and visited[nx][ny] < year:
                queue.append((nx,ny))
                visited[nx][ny] = year


    

def solution():
    global bfsResult
    year = 0
    iceberg, startX, startY, meltSet = defaultCondition()
    while True:
        if iceberg> 0:
            visited[startX][startY] = year
            bfs(startX, startY, year)

            # 빙산이 분리됨
            if iceberg != bfsResult:
                break
            else:
                bfsResult = 0

                # 1년이 지남
                year += 1
                for x, y, m in meltSet:
                    graph[x][y] = max(graph[x][y]-m, 0)
                iceberg, startX, startY, meltSet = defaultCondition()

                # 그전까지는 모두 0이 아니었고 모두 연결되어 있었는데
                # 1년이 지나니 다 0이 되어버림 = 동시에 모두 0이됨
                if iceberg == 0:
                    return '0'
        else:
            break
    return str(year)

print(solution())