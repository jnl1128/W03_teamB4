# 바이러스 # DFS
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input()) # 컴퓨터의 개수 # 노드의 개수
M = int(input()) # 연결된 컴퓨터 쌍의 개수 # 간선의 개수
computers = [[] for _ in range(N+1)]
visited = [0 for i in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split(' '))
    computers[start].append(end)
    computers[end].append(start) # 순서가 중요하지 않고 # dfs로 탐색하다보면 9 1 로 주어지는 경우에 놓칠 수 있음.
    

cnt = 0
def dfs(start):
    global cnt
    cnt += 1
    visited[start] = 1
    for computer in computers[start]:
        if visited[computer] != 1:
            dfs(computer)
            

dfs(1)
print(f'{cnt-1}') # 본인을 빼줘야 함