import sys,copy
from collections import deque

input=sys.stdin.readline
N,M=map(int,input().strip().split())

A=[]
for i in range(N):
    A.append(list(map(int,(input().strip().split()))))
A2=copy.deepcopy(A) # 빙산을 녹이는 map하나 녹이는 기준을 세울 map하나 해서 A, A2 두개를 사용

direction=[(1,0),(-1,0),(0,1),(0,-1)] # 빙산 주변의 0을 찾기 위한 방향키

def check_block(visited,dq): # 빙산이 동강났는지 확인하기 위한 함수
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
            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==1: # 이미 방문이 된 곳인지 확인 - 얼음이 있는 위치인지
                visited[nx][ny]=0 # 얼음이 있으면 확인하고 체크한거 표시
                block+=1 # 블럭 개수 +1
                temp.append((nx,ny))
    return block, dq


def find_ice(dq,visited): # 초기 빙산의 개수 파악
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
    visited=[[0]*M for _ in range(N)] # 빙산을 체크하면서 visited가 1로 바뀜
    find_ice(dq,visited)      
    if len(dq) != check_block(visited,dq)[0]: # 처음 두덩이로 들어오는 빙산이 존재함 이를 카운트하기 위한 함수
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
