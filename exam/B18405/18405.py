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
                virus.append([table[i][j],0,i,j])

def solve():
    check_virus()
    virus.sort()
    dq=deque(virus)
    while dq:
        v,t,c,r=dq.popleft()
        if t == s:
            print(table[x-1][y-1])
            break
        for dc, dr in direction:
            nc=c+dc
            nr=r+dr
            if 0<=nc<N and 0<=nr<N and table[nc][nr]==0:
                table[nc][nr]=v
                dq.append((v,t+1,nc,nr))
        if len(dq)==0:
            print(table[x-1][y-1])
            break

      
solve()