import sys
from collections import deque
sys.setrecursionlimit(10**8)

input=sys.stdin.readline

N,M= map(int,input().strip().split()) 

A=[]
for i in range(N): # 미로의 정보를 받음
    A.append(list(map(int,input().strip())))

dx=[-1,1,0,0] # 4방향 탐색을 해야하기때문에 방향 확인
dy=[0,0,-1,1]

def bfs(x,y): # BFS 탐색
    dq=deque()
    dq.append((x,y))
    while dq:
        x, y=dq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or N<=nx or ny<0 or M<=ny:
                continue
            if A[nx][ny]==0:
                continue
            if A[nx][ny]==1:
                A[nx][ny]=A[x][y]+1
                dq.append((nx,ny))
    return A[N-1][M-1]



print(bfs(0,0)) # 시작하는 지점은 0,0



