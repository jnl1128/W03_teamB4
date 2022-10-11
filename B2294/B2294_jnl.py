# 동전2 #그리디하게 #다익스트라
import sys , heapq
input = sys.stdin.readline
print = sys.stdout.write

N,K = map(int, input().split(' '))
coins = set()
for _ in range(N):
    coins.add(int(input()))
# 인덱스 = 동전의 합
# 값 = 인덱스만큼의 동전의 합을 만들기 위해 필요한 최소한의 동전 개수
dp = [sys.maxsize for _ in range(100001)]

def dijkstra():
    H = []
    global K
    for coin in coins:
        heapq.heappush(H, (1, coin))
        dp[coin] = 1
    while H:
        # x: 지금까지 동전의 합
        d, x = heapq.heappop(H)
        if x < K:
            for coin in coins:
                if x + coin < K:
                    # 해당 동전의 합(x+coin)을 만드는 동전의 개수가 더 적은게 발견됐다면
                    if dp[x+coin] > d+1:
                        dp[x+coin] = d+1
                        heapq.heappush(H, (d+1, x+coin))
                elif x + coin == K:
                    return str(d+1)
    return '-1'
    

print(dijkstra())

