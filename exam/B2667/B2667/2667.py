import sys
from collections import deque

input=sys.stdin.readline

N=int(input())

table=[]
for i in range(N):
    table.append(list(map(int,list(input().strip()))))
direction=[(1,0),(-1,0),(0,1),(0,-1)]        
cnt=0
block=[]

dq=deque()
for i in range(N):
    for j in range(N):
        if table[i][j]==1:
            dq.append((i,j))
            cnt+=1                
            block_temp=0
            while dq: 
                x,y=dq.popleft()                    
                for dx, dy in direction:
                    nx=x+dx
                    ny=y+dy
                    if table[x][y]==1:
                        table[x][y]=0
                        block_temp+=1

                    if 0<=nx<N and 0<=ny<N and table[nx][ny]==1:
                        table[nx][ny]=0
                        block_temp+=1
                        dq.appendleft((nx,ny))
            block.append(block_temp)



print(cnt)
print(*sorted(block),sep='\n')
        