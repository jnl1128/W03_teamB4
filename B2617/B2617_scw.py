import sys
from collections import deque,defaultdict

input=sys.stdin.readline

N, M=map(int,input().strip().split())

small_list=defaultdict(list) # small을 기준으로 잡은 list 
big_list=defaultdict(list) # big을 기준으로 잡은 list
for i in range(M):
    a,b = map(int,input().strip().split())
    big_list[a].append(b)
    small_list[b].append(a)

mid=(N+1)//2 # 홀수개가 들어오기 때문에 중간부는 (N+1)//2 임

def dfs(array,start):
    cnt=0
    visited[start]=1 # 처음 들어온 위치에 방문 체크
    dq=deque()
    dq.append(start) # 큐에 append
    while dq:
        x=dq.popleft()
        for i in array[x]:
            if visited[i]==0: # 방문하지 않은거 즉 dic에서 무게 체크를 하지 않은 경우
                cnt+=1 # 카운트 개수 올리고
                visited[i]=1 # 방문 처리
                dq.append(i) # 방문 처리 한 애를 넣고 다시 다음 무게 체크를 할 것임
    return cnt # dfs 탈출하면 cnt 값을 리턴


answer=0
for i in range(1,N+1): # 구슬이 1번부터 N개까지 있다고 했으니깐 1번부터 돌림
    visited=[0]*(N+1) # 구슬이 들어올때마다 새로운 체크 리스트가 필요함
    if dfs(big_list,i)>=mid:
        answer+=1
    if dfs(small_list,i)>=mid:
        answer+=1
print(answer)

# ref: https://campkim.tistory.com/17