import sys
from collections import defaultdict,deque
sys.setrecursionlimit(10**8)

input=sys.stdin.readline

N=int(input())
M=int(input())
A=defaultdict(list)
visited=[0]*(N+1) # 간선을 받은 갯수를 파악하기 위한 visited
visited2=[[0]*(N+1) for _ in range(N+1)] # 가중치를 계산하기 위한 visited2
for i in range(M):
    a,b,c=map(int,input().strip().split())    
    A[b].append([a,c]) # 기본 부품(b) 이 중간부품(a)를 만드는데 필요한 개수(c)
    visited[a]+=c # 중간부품(a)의 간선 개수 (c)

for key in A: # dictionary 를 정렬
    A[key].sort()

def topologySort(): # 위상정렬
    dq=deque()
    for key in A.keys(): # 진입 노드 append하고
        if visited[key]==0:
            dq.append(key)

    while dq:
        x=dq.popleft() # 하나씩 빼고
        for i in A[x]:
            if visited2[x].count(0)==N+1: # 기본 부품은 그 value가 전부 0일테니 0인 개수가 N+1개와 같은걸로 확인 가능
                visited2[i[0]][x]+=i[1] # 기본 부품이면 가중치 넣어주고
            else:
                for j in range(1,N+1): # 중간부품이면 기본부품의 개수를 다 파악해서 넣어주기
                    visited2[i[0]][j]+=visited2[x][j]*i[1] # 중간부품 = 기본부품 * 필요 개수
            
            visited[i[0]]-=i[1] # 간선 지우기
            
            if visited[i[0]]==0 and i[0] !=N: # 간선이 0이된 것을 append 만약 완성품을 넣게되면 error 발생
                dq.append(i[0])

topologySort()
for i, nums in enumerate(visited2[N]):
    if nums>0:
        print(i, nums)