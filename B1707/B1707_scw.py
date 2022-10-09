import sys
from collections import defaultdict
# from collections import deque # BFS 방법을 위한 deque import
sys.setrecursionlimit(10**8)

input=sys.stdin.readline

def dfs(start, color): # dfs 함수 받는것 - key, color info
    global flag # flag가 true로 끝나면 YES 아니면 NO
    if visited[start]==0: # 들어온 start가 한번도 방문한적(색이 칠해진적) 없다면 시작
        visited[start]=color  # 색을 칠해주고
        for i in line_info[start]: # start를 key로하는 dic value를 돌림
            if visited[i] !=0: # 그중 0이 아닌 애가 있으면
                if visited[i]==visited[start]: # 근데 걔가 start랑 같은 색이면 = 인접한 노드가 같은색이다
                    flag=False # 인접한 노드가 같으면 안되니 false
                    return
            else:
                dfs(i,color*(-1)) # 인접한 노드가 같지 않고 + visited[key] ==0 이면

# def bfs(start, color): # BFS
#     global flag 
#     dq=deque()
#     dq.append(start) # 처음 스타트 값을 dq에 넣어줌
#     visited[start]=color # 그 스타트에 해당하는 visited를 color로 색칠
#     while dq:
#         x=dq.popleft() # 꺼내고
#         for i in line_info[x]: # 그 값을 key로갖는 value를 돌리고
#             if visited[i]==0: # 그게 0이면 한번도 안가본거니깐 색칠 ㄱ
#                 dq.append(i)
#                 visited[i]= -1*visited[x] # 칠할땐 인접한 색이랑 다른 색으로
#             elif visited[i]==visited[x]: # 둘이 같으면?
#                 flag=False # 끝난거임
#                 return



N=int(input().strip())

for _ in range(N):
    V,E=map(int,(input().strip()).split())
    line_info=defaultdict(list)
    for _ in range(E):
        a,b=map(int,(input().strip()).split())
        line_info[a].append(b)
        line_info[b].append(a)

    visited=[0]*(V+1)
    flag=True
    
    for key in line_info.keys(): # dfs는 dictionary key를 기준으로 돌리며 간선 연결이 끊어진 것들을 같이 돌리기 위해서 for문
        dfs(key,1)
    # for i in range(1,V+1): # BFS의 경우 key 로 돌리는 것이 아닌 visited 가 한번도 방문한 적이 없는 애들을 기준으로 running
    #     if not visited[i]:
    #         bfs(i,1)
    if flag == True:
        print("YES")
    else:
        print("NO")

