# 구슬 찾기 # 남의 풀이
import sys 
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split(' '))
smaller_lst = [[] for _ in range(N+1)]
bigger_lst = [[] for _ in range(N+1)]
mid = (N+1)//2

for _ in range(M):
    b, s = map(int, input().split(' '))
    bigger_lst[b].append(s)
    smaller_lst[s].append(b)

def dfs(arr, n):
    global cnt
    for m in arr[n]:
        if visited[m] != 1:
            visited[m] = 1
            cnt += 1
            dfs(arr, m)


answer = 0
for i in range(1, N+1):
    # i에 대해서 dfs를 2번 하기 때문에, 자신에 대해서는 visited 체크를 하지 않는다.
    # 같은 visited를 써도 되는 이유는 i보다 큰 값과 작은 값은 중복이 되지 않을 것이기 때문이다.
    visited = [0 for _ in range(N+1)]
    cnt = 0
    dfs(bigger_lst, i)
    if cnt >= mid:
        answer += 1
    cnt = 0
    dfs(smaller_lst, i)
    if cnt >= mid:
        answer += 1
print(f'{answer}')



