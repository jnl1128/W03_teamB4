import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

def dfs_find_outin(start, check_point):
    global visited
    cnt = 0
    if check_point == 0:
        visited[start] = True
        for i in graph[start]:
            if not visited[i]:
                if points[i] == '1':
                    cnt += 1
                elif points[i] == '0':
                    cnt += dfs_find_outin(i,0)
        return cnt
    else:
        for i in graph[start]:
            if points[i] == '1':
                cnt += 1
        return cnt

N = int(input())
A = input().strip()

visited = [False] * (N+1)
points = '.'+A
graph = [[] for _ in range(N+1)]
num_list = []
while True:
    try:
        a,b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    except:
        break

count = 0

for i in range(1, N+1):
    if points[i] == '0' and not visited[i]:
        tmp = dfs_find_outin(i, 0)
        count += (tmp * (tmp-1))
    elif points[i] == '1':
        tmp = dfs_find_outin(i, 1)
        count += tmp

print(count)