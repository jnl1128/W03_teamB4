# 트리의 부모 찾기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N = int(input())
nodes = [[] for _ in range(N+1)]
visited  = [0 for _ in range(N+1)]
result = [0 for _ in range(N+1)] # 각 인덱스들의 부모를 넣어둘 리스트
for _ in range(N-1):
    start, end = map(int,input().split(' '))
    nodes[start].append(end)
    nodes[end].append(start)

def dfs(parent):
    visited[parent] = 1
    for child in nodes[parent]:
        if visited[child] != 1:
            result[child] = parent
            dfs(child)

dfs(1)
print(*result[2:], sep='\n')