import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**8)

input=sys.stdin.readline


N,M,K,X = map(int,input().strip().split())

city=defaultdict(list)
for i in range(M): # 방향이 존재하기 때문에 한방향으로만 탐색이 가능(시작점이 존재)
    a,b=map(int,input().strip().split())
    city[a].append(b)
    #city[b].append(a)

# print(city)
visited=[False]*(N+1)
cnt=0
answer_list=[]
def bfs(X,cnt,K):
    dq=deque()
    dq.append((X,cnt))
    visited[X]=True
    while dq:
        a,cnt=dq.popleft()
        if cnt==K:
            answer_list.append(a)
    
        for i in city[a]:
            if visited[i]==False:
                dq.append((i,cnt+1))
                visited[i]=True

bfs(X,cnt,K)


# visited[X]=0
# print(answer_list)
# print(visited)
    
if len(answer_list)==0:
    print(-1)
else:
    answer_list.sort()
    print(*answer_list,sep='\n')