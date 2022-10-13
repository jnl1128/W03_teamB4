import sys,heapq
sys.setrecursionlimit(10**8)

input=sys.stdin.readline

M,N,H = map(int,input().rstrip().split())

A=[[list(map(int,input().strip().split())) for _ in range(N)] for _ in range(H)]

direction=[(1,0,0),(-1,0,0),(0,0,-1),(0,1,0),(0,-1,0),(0,0,1)]

def find_good(heap):
    global M,N,H,A
    a=0
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if A[z][y][x]==1:
                    heapq.heappush(heap,(a,z,y,x))
    return heap
    
def check_tomato(a):
    global M,N,H,A
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if A[z][y][x]==0:
                    print(-1)
                    exit(0)
    if z==H-1 and y==N-1 and x==M-1:
        print(a)


def bfs():
    global M,N,H,A
    heap=[]
    find_good(heap)
    a=None
    while heap:        
        a,z,y,x=heapq.heappop(heap)
        for dx,dy,dz in direction:
            nz=z+dz
            ny=y+dy
            nx=x+dx            
            if 0<=nz<H and 0<=nx<M and 0<=ny<N and A[z][y][x]==1:
                if A[nz][ny][nx]==0:
                    A[nz][ny][nx]=1
                    heapq.heappush(heap,(a+1,nz,ny,nx))
                else:
                    continue
    return check_tomato(a)



bfs()

