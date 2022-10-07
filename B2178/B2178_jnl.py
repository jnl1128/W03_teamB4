# 미로 탐색 # BFS
import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split(' '))
miro = []
for _ in range(N):
    miro.append(list(map(int, list(input().rstrip()))))

def bfs():
    queue = deque([[0, 0]])  
    # 현재 위치에서 움직일 수 있는 4가지 방향
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i] 
            ny = y+dy[i]
            # visited가 필요하지 않는 이유는 miro의 초기값이 + 연산으로 바뀌기 때문에
            # 1 or 0: not visited, else: visited
            if 0<=nx<N and 0<=ny<M and miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1 # 가는 순서대로 넣어주면 n,m에는 n,m까지 가는 최단 거리가 들어있게 됨
                queue.append([nx, ny])
    return miro[N-1][M-1]
            
print(f'{bfs()}')
