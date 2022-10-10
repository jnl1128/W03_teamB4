import sys
from collections import deque # BFS 사용을 위한 deque
import heapq # dijkstar 사용을 위한 heapq
sys.setrecursionlimit(10**8)

input=sys.stdin.readline

N=int(input())
A=[]
for i in range(N):
    A.append(list(map(int,list(input().strip()))))

dx=[1,0,-1,0] # 상하좌우 탐색을 위한 좌표
dy=[0,1,0,-1]

# def bfs(x,y):
#     dq=deque()
#     dq.append((x,y))
#     visited=[[-1]*N for _ in range(N)] # 미로를 탐색하는 경로 -1은 나올수가 없는 숫자이므로 탐색 자리를 전부 -1로 초기화
#     visited[0][0]=0 # 첫 시작을 0으로 시작 앞으로 지나가는길은 0으로 동작
#     while dq:
#         x, y=dq.popleft()
#         if x== N-1 and y==N-1:
#             return visited[x][y] # 목적지에 도달하면 그때의 값을 return

#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]
#             if 0<=nx<N and 0<=ny<N and visited[nx][ny]==-1:
#                 if A[nx][ny]==1:
#                     dq.appendleft((nx,ny)) # 흰방 탐색을 먼저하기 위해서 appendleft 사용
#                     visited[nx][ny]=visited[x][y] # 흰방은 방을 안부숴도 되니깐 그대로 input
#                 else:
#                     dq.append((nx,ny)) # 검은 방은 뒤에다 append 나중에 탐색하게
#                     visited[nx][ny]=visited[x][y]+1 # 검은방은 부숴야하니깐 부순 횟수 1 추가


# print(bfs(0,0))

##################### 다익스트라 사용
def dijkstar(a,x,y):
    heap=[]
    heapq.heappush(heap,(a,x,y))
    visited=[[-1]*N for _ in range(N)]
    visited[x][y]=0
    while heap:
        a, x, y=heapq.heappop(heap) # a 는 검은 방을 부순 후 진입한 곳을 체크
        if x== N-1 and y==N-1:
            return visited[x][y] # 목적지에 도달하면 그때의 값을 return // a를 return 해도 됨

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==-1:
                if A[nx][ny]==1:
                    heapq.heappush(heap,(a,nx,ny)) # 흰방은 그냥 넣어도 됨
                    visited[nx][ny]=visited[x][y] # 흰방은 방을 안부숴도 되니깐 그대로 input
                else:
                    heapq.heappush(heap,(a+1,nx,ny)) # a번 부순 검은방에 +1
                    visited[nx][ny]=visited[x][y]+1 # 검은방은 부숴야하니깐 부순 횟수 1 추가

print(dijkstar(0,0,0))