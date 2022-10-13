import sys,heapq
from collections import defaultdict

input=sys.stdin.readline

N,M=map(int,input().strip().split())
table=defaultdict(list)
for i in range(M):
    a,b,c= map(int,input().strip().split())
    table[a].append([c,b]) # 중량을 기준으로 최대힙을 사용할 것이기 때문에 금액으로 내림차순 정렬
    table[b].append([c,a]) # 양방향으로 다닐수 있으므로 양방향으로 같이 만들어준다

s,e=map(int,input().strip().split())

for key in table:
    table[key].sort(key=lambda x:x[1], reverse=True) # 내림차순 정렬



def dijkstra(start) :
    heap=[]
    heapq.heappush(heap,(0,start)) # 초기 출발은 중량을 0으로 출발함

    while heap:
        weight,x =heapq.heappop(heap)
        weight=-1*weight # 최대힙을 사용할것이기 때문에 -1을 곱해준다
        
        if visited[x]>weight : continue # 방문한 도시의 중량이 비교할 중량보다 크면 무시

        for i in table[x]: 
            if weight==0: # 중량이 0일경우 방문한 도시에 현재 중량을 넣어줌
                visited[i[1]]=i[0]
                heapq.heappush(heap,(-visited[i[1]],i[1])) # 그리고 push
            elif visited[i[1]]<i[0] and visited[i[1]]<weight:
                visited[i[1]]=min(weight,i[0])
                heapq.heappush(heap,(-visited[i[1]],i[1]))
       
            

visited=[0]*(N+1)

dijkstra(s)

print(visited[e])


