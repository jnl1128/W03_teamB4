import sys
from collections import defaultdict
sys.setrecursionlimit(10**8)

input=sys.stdin.readline

N=int(input())

A=list(map(int,(list(input().strip()))))
A=[0]+A

walking=defaultdict(list)

while 1:
    try:
        a,b=map(int,input().strip().split())
        walking[a].append(b)
        walking[b].append(a)
    except:
        break

def solve():
    count =0 # 최종 경우의 수 출력
    visited=[0]*(N+1) # 방문된 곳이 겹치는지 확인

    def dfs(x): # DFS 함수
        cnt=0 # DFS 함수 내에서 실내를 만나는 경우의 수 세기
        for i in walking[x]:
            if A[i]==1: # 실내를 만날때마다 cnt +1
                cnt+=1
            else:
                if visited[i]==0: # 실외 옆에 또 실외가 있으면
                    visited[i]=1 # 거기도 방문처리 하고
                    cnt+=dfs(i) # 옮겨간 실외를 기준으로 다시 실내를 찾기
        return cnt
    
    for i in range(1,N+1):
        if A[i]==1: # list[A]에서 바로 인접한 실내가 있는 경우 실내-실내로 바로 +1
            for j in walking[i]:
                if A[j]==1:
                    count+=1
        else:
            if visited[i]==0: # 인접한 곳이 실외 인경우
                visited[i]=1 # 방문해주고
                Temp=dfs(i) # 실외를 기준으로 실내를 찾기위한 dfs 탐색
                count+=Temp*(Temp-1) # 시작점과 끝점이 바뀌면 다른 경우로 count 되기 때문에 팩토리얼로 두개를 선택하는 경우의수

    return count

print(solve())