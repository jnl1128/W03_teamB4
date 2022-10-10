import sys,heapq
from collections import defaultdict
sys.setrecursionlimit(10**8)

input=sys.stdin.readline

N=int(input())

M=int(input())

# 최소힙을 사용하면 pop을 할때 항상 최소비용을 꺼낼수 있음
def dijkstra(start) : # heapq를 이용한 다익스트라 구현 - for문 두개를 사용하면 시간복잡도가 N**2 인데 heapq를 사용하면 NlogN
    visited[start]=0
    heap=[]
    heapq.heappush(heap,(start,0)) # 힙에 첫 시작점과 비용 0을 넣음 (내가 나한테 가는건 0원)

    while heap:
        x,cost_val =heapq.heappop(heap) # pop을 하고
        if visited[x]<cost_val : continue # vistied에 있는 비용이 pop한 비용보다 작으면 그냥 무시
        for i in costs[x]: # 그리고 costs table에 있는 i를 돌려서
            next=i[0] # i 의 0번 x에서출발해서 i로 도착하는 도시
            next_cost=cost_val+i[1] # 도착하는 도시까지의 비용
            if next_cost<visited[next]: # 그 비용이 기존의 주어진 비용보다 적으면
                visited[next]=next_cost # 새로운 비용으로 업데이트
                heapq.heappush(heap,(next,next_cost)) # 업데이트 된 비용을 heapq로 push




costs=defaultdict(list)
for _ in range(M):
    a,b,c=map(int,input().strip().split())
    costs[a].append([b,c])
start,end=map(int,input().strip().split())


visited=[999999999999]*(N+1)

dijkstra(start)

print(visited[end])