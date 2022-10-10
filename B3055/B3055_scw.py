import sys
from collections import deque
sys.setrecursionlimit(10**8)

input=sys.stdin.readline

R,C=map(int,input().strip().split()) # 열과 행 정보를 받음

A=[]
for i in range(R):
    A.append(list(input().strip())) # map 정보를 받음

def find_someting(visited,dotch,water): # map에 표기된 정보를 받으면서 있는 위치를 visit 표시
    for i in range(R):
        for j in range(C):
            if A[i][j]=='S':
                dotch.append([i,j])
                visited[i][j]=1
            if A[i][j]=='*':
                water.append([i,j])
                visited[i][j]=1
            if A[i][j]=='X':
                visited[i][j]=1
    return visited, dotch, water

def moving(): # 고슴도치 움직이는 함수
    cnt=0
    visited=[[0]*C for _ in range(R)] # visit tracking 
    dotch=deque()
    water=deque()
    direction=[(1,0),(0,1),(-1,0),(0,-1)] # 방향키
    find_someting(visited,dotch,water) # map에 표기된 정보 받기
    while dotch: # 고슴도치 큐가 존재하면 while 진입
        for _ in range(len(water)): # 처음에 물이 들어있는 횟수만큼 돌리고 - while로 하면 물만 계속 돈다
            water_x, water_y=water.popleft()
            for dx,dy in direction:
                N_w_x=water_x+dx
                N_w_y=water_y+dy
                if 0<=N_w_x<R and 0<=N_w_y<C:
                    if A[N_w_x][N_w_y]=='.': # 물이 있는 위치 확장
                        water.append([N_w_x,N_w_y])
                        A[N_w_x][N_w_y]='*'
                        visited[N_w_x][N_w_y]=1
        cnt+=1 # 물 움직임 끝났으면 시간 지남 - 고슴도치 움직일때까지 기다리면 탈출 --> 시간이 증가 이런 형식이 발생
        for _ in range(len(dotch)):
            dotch_x, dotch_y=dotch.popleft()
            for dx,dy in direction:
                N_d_x=dotch_x+dx
                N_d_y=dotch_y+dy
                if 0<=N_d_x<R and 0<=N_d_y<C and visited[N_d_x][N_d_y]==0: # 고슴도치 움직임
                    if A[N_d_x][N_d_y]=='.':
                        dotch.append([N_d_x,N_d_y])
                        visited[N_d_x][N_d_y]=1
                    elif A[N_d_x][N_d_y]=='D': # 목적지 닿으면 끝
                        return print(cnt)

    return print("KAKTUS") # 목적지 닿기 전에 죽음

moving()
