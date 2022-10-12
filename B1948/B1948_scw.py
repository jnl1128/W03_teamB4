import sys
from collections import defaultdict, deque

input=sys.stdin.readline
N=int(input().strip())
M=int(input().strip())

road_info=defaultdict(set)
re_road_info=defaultdict(set)
edge=[0]*(N+1) # 간선을 받은거 indgree
check=[0]*(N+1) # 역 탐색할때 지나온 도시 체크
result_time=[0]*(N+1)

for i in range(M):
    a,b,c =map(int, input().strip().split())
    road_info[a].add((b,c)) # 출발 - 도착 - 시간
    re_road_info[b].add((a,c)) # 역탐색을 위한 re_road
    edge[b]+=1 # 간선을 받은 정보 입력

s,e=map(int, input().strip().split()) # start, end 값을 입력

def topologySort(s,e):
    dq=deque()
    dq.append(s) # 정방향 먼저
    while dq:
        x=dq.popleft()
        for city, time in road_info[x]:
            edge[city]-=1
            result_time[city]=max(result_time[city],result_time[x]+time) # 각 도시까지 오는데 최대 시간을 누적
            if edge[city]==0:
                dq.append(city)

    dq.append(e)
    cnt=0 # 7번은 0번째 도시로 역으로 지나가면서 만나는 도시 개수 = 도로 개수
    while dq:
        x=dq.popleft()
        for city, time in re_road_info[x]:
            if time==result_time[x]-result_time[city]: # 해당 도시까지 도착하는데 걸리는 최대시간 - 현재 도시까지의 걸리는 시간을 한 것이 dic의 시간과 같으면 max와 동일한 경로
                cnt+=1 # 따라서 도시 개수 누적 = 도로 개수 누적
                if check[city]==0 :
                    dq.append(city)
                    check[city]=1 # 해당 도시 체크 - 중복 제거

    print(result_time[e])
    print(cnt)

            
topologySort(s,e)

# ref : https://hiruby.tistory.com/439