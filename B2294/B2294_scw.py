import sys
input=sys.stdin.readline

n, k = map(int, input().split())
coins = []
dp = [0 for _ in range(k + 1)] # 각 공간(목표 금액)마다 사용되는 코인의 개수를 저장
for i in range(n):
    coins.append(int(input()))
for i in range(1, k + 1):
    temp = []
    for coin in coins:
        if coin <= i and dp[i - coin] != -1:
            temp.append(dp[i - coin])
    if not temp: # 목표 금액이 coin으로 나눠떨어지지 않았으면 -1
        dp[i] = -1
    else:
        dp[i] = min(temp) + 1 # 나눠떨어지면 뺀것에 +1= 동전개수
print(dp[k]) # 목표 금액에 도달했을때의 동전 개수를 출력

# 아래 방법을 사용하면 최대 코인의 크기를 다양한 개수로 사용하지 못하는 문제가 생김
# n,k=map(int,input().strip().split())

# A=[]
# for i in range(n):
#     A.append(int(input()))
# A.sort()

# A=[0]+A

# def dfs(x,k):
#     global answer
#     dq=deque()
#     dq.append(x)
#     while dq:
#         x=dq.popleft()
#         visited[x]=1
#         a=k//A[x]
#         k=k-a*A[x]
#         answer+=a
#     if visited[x-1]==0:
#         dfs(x-1,k)
#     return k
    


# answer_min=99999999999
# check=[1]*(n+1)
# for i in range(n,0,-1):
#     visited=[0]*(n+1)
#     visited[0]=1
#     answer=0
#     check[i]=dfs(i,k)
#     answer_min=min(answer,answer_min)

# if 0 in check:
#     print(answer_min)
# else:
#     print(-1)
