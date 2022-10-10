import sys,heapq
from collections import defaultdict
sys.setrecursionlimit(10**8)

input=sys.stdin.readline

N=int(input())

M=int(input())


def dijkstra(start) :
    visited[start]=0
    heap=[]
    heapq.heappush(heap,(start,0))

    while heap:
        x,cost_val =heapq.heappop(heap)
        if visited[x]<cost_val : continue        
        for i in costs[x]:
            next=i[0]
            next_cost=cost_val+i[1]
            if next_cost<visited[next]:
                visited[next]=next_cost
                heapq.heappush(heap,(next,next_cost))




costs=defaultdict(list)
for _ in range(M):
    a,b,c=map(int,input().strip().split())
    costs[a].append([b,c])
start,end=map(int,input().strip().split())


visited=[999999999999]*(N+1)

dijkstra(start)

print(visited[end])