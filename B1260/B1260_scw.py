import sys
from collections import deque, defaultdict
sys.setrecursionlimit(10**8)

def dfs(v): # DFS 탐색 실시
    print(v,end=' ') # 진입 도시 출력
    visit[v]=1 # 진입한 도시 체크
    for next in A[v]: # 1번부터 N번까지 돌리면서
        if visit[next]==0: # 방문하지 않았으면서 + 해당 dic 안에 존재하면
            dfs(next) # 재귀 ㄱㄱ

def bfs(v): # BFS 탐색 실시
    dq=deque() # popleft를 사용하기 위해서 큐 형식으로 저장
    dq.append(v) # 진입 도시 append 해주고
    visit[v]=1 # 진입한 도시 체크
    while dq: # 큐에 데이터가 있으면
        a=dq.popleft() # 제일 앞에꺼 빼주고 <-- 이전에 방문한 도시
        print(a,end=' ') # 방문했던 도시 출력
        for i in A[a]: # a dic에 있는 것을 순서대로 돌리면서 방문 함
            if not visit[i]:
                dq.append(i)
                visit[i]=1

input = sys.stdin.readline

N,M,k=map(int,input().strip().split())

A=defaultdict(list)


for i in range(M): # 데이터 input, dic 형태로
    city1,city2=map(int,input().strip().split())
    A[city1].append(city2)
    A[city2].append(city1)


for i in A: # dic 형태로 받은 데이터 value 부분 정렬    
    A[i].sort()

# print(A)

visit=[0]*(N+1) # 방문할 도시들 만들어주고

if N==1:
    print(1)
    print(1)
else:
    dfs(k)
    print()
    visit=[0]*(N+1)
    bfs(k)

# for i in range(M): # 데이터 input, dic 형태로
#     city1,city2=map(int,input().strip().split())
#     if city1 != city2 and city1 !=" " and city2 !=" ":
#         if city1 in A and city2 not in A[city1]:
#             A[city1].append(city2)
#         elif city1 not in A:
#             A[city1]=[city2]
#         else:
#             continue
#         if city2 in A and city1 not in A[city2]:
#             A[city2].append(city1)
#         elif city2 not in A:
#             A[city2]=[city1]
#         else:
#             continue