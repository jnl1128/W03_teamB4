# 토마토 #뭔가 느낌 다익스트라
import sys , heapq
input = sys.stdin.readline
print = sys.stdout.write

M, N, H = map(int, input().split(' '))
visited = [[[-2] * M for _ in range(N)] for _ in range(H)]
graph = []
for _ in range(H):
    tmp = []
    for _ in range(N):
        tmp.append(list(map(int, input().split(' '))))
    graph.append(tmp)
dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [-1, 1, 0, 0, 0, 0]

# 시작 지점 정하기
def getDone():
    done = []
    empty = 0
    notdone = 0
    for z in range(H):
        for x in range(N):
            for y in range(M):
                if graph[z][x][y] == 1:
                    done.append([z, x, y])
                    visited[z][x][y] = 0
                elif graph[z][x][y] == -1:
                    empty += 1
                else:
                    notdone += 1
    return done, empty, notdone

def getNotDone():
    cnt = 0
    maxDays = -3
    for z in range(H):
        for x in range(N):
            for y in range(M):
                maxDays = max(maxDays, visited[z][x][y])
                if visited[z][x][y] < 0:
                    cnt += 1
    return cnt, maxDays

def dijkstra():
    heap = []
    done, empty, notdone = getDone()
    if notdone == 0:
        return '0'

    for z, x, y in done:
        heapq.heappush(heap, [visited[z][x][y], z, x, y])
    while heap:
        _, z, x, y = heapq.heappop(heap)
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nz<H and 0<=nx<N and 0<=ny<M and visited[nz][nx][ny] == -2:
                if graph[nz][nx][ny] == -1 or graph[nz][nx][ny] == 1:
                    continue
                else:
                    visited[nz][nx][ny] = visited[z][x][y] + 1
                    heapq.heappush(heap, [visited[nz][nx][ny], nz, nx, ny])
    resultNotDone, maxDays = getNotDone()
    if empty < resultNotDone:
        return '-1'
    return str(maxDays)
print(dijkstra())