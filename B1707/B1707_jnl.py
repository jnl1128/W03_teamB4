# 이분 그래프
import sys
from collections import defaultdict
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10 ** 9)

def dfs(start, color):
    global flag # 인접한 두 정점이 같은 색인지
    if colors[start] == 0:
        colors[start] = color # 방문한 적이 없다면 color를 저장해주기
        for next in nodes[start]:
            if colors[next] != 0: # 방문한 적이 있다면(== color를 지정해 준 적이 있다면) color가 같은지
                if colors[next] == colors[start]:
                    flag = False
                    return 
            else: # 방문한 적이 없다면 해당 노드에 대해서 dfs 호출
                dfs(next, color*-1)
    

#
N = int(input())
for _ in range(N):
    V, E = map(int, input().split(' '))
    nodes = defaultdict(list)
    colors = [0 for _ in range(V+1)] # 이분 그래프가 되기 위해서는 2가지 색만으로도 인접한 노드들이 서로 다른 색이 되도록 칠할 수 있어야 한다.
    # 내 코드에선 초기의 모든 색은 0이고 1 또는 -1이라는 2가지 색으로 칠할 것
    # colors가 visited의 역할도 함께
    flag = True
    for _ in range(E):
        start, end = map(int, input().split(' '))
        nodes[start].append(end)
        nodes[end].append(start)
    for key in nodes: # 비연결 리스트라면 dfs() 재귀만으로는 이분 그래프인지 탐색할 수 없음
        dfs(key, 1)
    if flag:
        print('YES\n')
    else:
        print('NO\n')