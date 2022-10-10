# 탈출
import sys, heapq
input = sys.stdin.readline
print = sys.stdout.write
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
R, C = map(int, input().split(' '))
visited = [[-1]*C for _ in range(R)]
graph = []
for _ in range(R):
    graph.append(list(input().rstrip()))

def willBeWater(r, c):
    for i in range(4):
        nr = dr[i] + r
        nc = dc[i] + c
        if 0<=nr<R and 0<=nc<C and graph[nr][nc] == '*':
            return True
    return False

def watered():
    pos = []
    for r in range(R):
        for c in range(C):
            if graph[r][c] == '*':
                for i in range(4):
                    nr = dr[i]+r
                    nc = dc[i]+c
                    if 0<=nr<R and 0<=nc<C and graph[nr][nc] == '.':
                        pos.append([nr, nc])
    for r, c in pos:
        graph[r][c] = '*'

def getPosition():
    startR= startC =0
    for r in range(R):
        for c in range(C):
            if graph[r][c] == 'S':
                startR, startC = r, c
    return startR, startC

def dijkstra():
    startR, startC = getPosition()
    visited[startR][startC] = 0
    H = []
    minute = 0
    heapq.heappush(H, [visited[startR][startC], startR, startC])
    while H:
        m, r, c = heapq.heappop(H)
        if m > minute:
            watered()
            minute = m
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<R and 0<=nc<C and visited[nr][nc] == -1:
                if graph[nr][nc] == '.' and not willBeWater(nr, nc):
                    visited[nr][nc] = visited[r][c] + 1
                    heapq.heappush(H, [visited[nr][nc], nr, nc])
                elif  graph[nr][nc] == 'D':
                    print(str(visited[r][c] + 1))
                    return 
    print('KAKTUS')
    
dijkstra()