import sys
from collections import deque
input=sys.stdin.readline

N,K=map(int,input().strip().split())

table=[]
for i in range(N):
    table.append(list(map(int,input().strip().split())))

s,x,y=map(int,input().strip().split())
direction=[(1,0),(-1,0),(0,1),(0,-1)]

virus=[]
def check_virus():
    for i in range(N):
        for j in range(N):
            if table[i][j]!=0:
                virus.append([table[i][j],0,i,j]) # 바이러스 값, 시간, 좌표 순서

def solve():
    check_virus()
    virus.sort() # 바이러스 값을 기준으로 정렬
    dq=deque(virus)
    while dq:
        v,t,c,r=dq.popleft()
        if t == s: # 정해진 시간이 되면 해당 테이블의 값을 출력하고 끝냄
            print(table[x-1][y-1])
            break
        for dc, dr in direction:
            nc=c+dc
            nr=r+dr
            if 0<=nc<N and 0<=nr<N and table[nc][nr]==0: # 방향체크해서 전염 시킴
                table[nc][nr]=v
                dq.append((v,t+1,nc,nr))
        if len(dq)==0: # 시간이 되기전에 큐가 비어버리면 해당 위치의 값을 반환하고 끝냄
            print(table[x-1][y-1])
            break

      
solve()