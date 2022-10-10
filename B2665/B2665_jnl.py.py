from heapq import heappush, heappop
N = int(input())
visited = [[-1]*N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = []
for _ in range(N):
    graph.append(list(map(int, list(input()))))

def dijkstra():
    H = []
    visited[0][0] = 0
    heappush(H ,[0, 0, 0])
    while H:
        # c: 검은방 개수
        _, x, y = heappop(H)
        d_graph = []
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0 <=ny<N:
                d_graph.append([graph[nx][ny], nx, ny])

        for nc, nx, ny in d_graph:
            if visited[nx][ny] == -1:
                if nc == 1: # 흰방
                    visited[nx][ny] = visited[x][y]
                else: # 검은방
                    visited[nx][ny] = visited[x][y] + 1
                heappush(H, [visited[nx][ny], nx, ny])

    return str(visited[N-1][N-1])

print(dijkstra())