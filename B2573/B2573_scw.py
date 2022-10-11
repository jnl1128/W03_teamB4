import sys,copy
from collections import deque

input=sys.stdin.readline
N,M=map(int,input().strip().split())

A=[]
for i in range(N):
    A.append(list(map(int,(input().strip().split()))))
A2=copy.deepcopy(A)

direction=[(1,0),(-1,0),(0,1),(0,-1)]

def check_block(visited,dq):
    global A, A2
    x,y= dq.popleft()
    dq.append((x,y))

    temp=deque()
    block=1
    temp.append((x,y))
    visited[x][y]=0
    while temp:
        x,y=temp.popleft()
        for dx, dy in direction:
            nx=x+dx
            ny=y+dy
            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==1:
                visited[nx][ny]=0
                block+=1
                temp.append((nx,ny))
    return block, dq


def find_ice(dq,visited):
    global A, A2
    for i in range(N):
        for j in range(M):
            if A[i][j] != 0:
                dq.append((i,j))
                visited[i][j]=1
    return dq, visited


def solve():
    global A, A2
    dq=deque()
    cnt=0
    visited=[[0]*M for _ in range(N)]
    find_ice(dq,visited)    
    # x,y=dq.popleft()
    # dq.appendleft((x,y))    
    if len(dq) != check_block(visited,dq)[0]:
        return print(cnt)
    visited=[[0]*M for _ in range(N)]
    while dq:
        for _ in range(len(dq)):
            x,y =dq.popleft()            
            for dx, dy in direction:
                nx=x+dx
                ny=y+dy
                if 0<=nx<N and 0<=ny<M and A[nx][ny]==0 and A2[x][y]>0:
                    A2[x][y]-=1
            if A2[x][y] >0:
                dq.append((x,y))
                visited[x][y]=1
        cnt+=1

        if len(dq)==0:
            return print(0)
        elif len(dq) != check_block(visited,dq)[0]:
            return print(cnt)
            
        A=copy.deepcopy(A2)
        
    

solve()
