import sys
from collections import deque
sys.setrecursionlimit(10**8)

input=sys.stdin.readline

N=int(input())

A=[]
for i in range(N):
    A.append(list(map(int,list(input().strip()))))

print(A)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    cnt=0
    dq=deque()
    dq.append((x,y))
    while dq:
        x, y=dq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or N<=nx or ny<0 or N<=ny:
                continue
            if A[nx][ny]==0:
                continue
            if A[nx][ny]==1:
                A[nx][ny]=A[x][y]+1
                dq.append((nx,ny))
    return cnt

bfs(0,0)