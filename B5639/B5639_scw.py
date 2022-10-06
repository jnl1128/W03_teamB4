# import sys

# input=sys.stdin.readline

# A=[]
# while True:
#     try:
#         Node=int(input())
#         A.append(Node)
#     except:
#         break
# stack=[]
# answer_list=[]
# for i in range(len(A)-1):
#     if A[i+1]<A[i]:
#         stack.append(A[i+1])
#     elif stack[-1]<A[i+1]:
#         answer_list.append(stack.pop())
#         answer_list.append(A[i+1])
#         if stack==[]:
#             continue
#     stack.append(A[i+1])
#         # else:
#         #     answer_list.append(stack.pop())

# # print(answer_list)
# # print(stack)


# import sys
# sys.setrecursionlimit(10**9)
# nums = []
# while True:                            
#     try:
#         nums.append(int(sys.stdin.readline()))
#     except:
#         break
        
# def postorder(s, e):
#     if s > e:
#         return
#     mid = e + 1                         # 오른쪽 노드가 없을 경우

#     for i in range(s+1, e+1):
#         if nums[s] < nums[i]:
#             mid = i
#             break

#     postorder(s+1, mid-1)               # 왼쪽 확인
#     postorder(mid, e)                   # 오른쪽 확인
#     print(nums[s])

# postorder(0, len(nums)-1)


import sys
sys.setrecursionlimit(10**9) # 재귀 level이 너무 높아져서 limit가 걸린걸 풀어줘야함
input=sys.stdin.readline

A=[]
while True:
    try:
        Node=int(input()) # input을 계속 받고
        A.append(Node)
    except: # 더이상 input이 없으면 에러가 뜨는데 그때 break
        break

def solve(start,end):
    if start>end: # 둘이 역전되는 순간을 return 함 --> 이때의 start를 출력
        return
    mid=end+1 # 뒷단에서 후위순회를 할때 오른쪽 트리가 없으면 재귀를 바로 탈출하게 하기 위해서

    for i in range(start+1, end+1): # root를 제외하고 범위 끝까지 for문을 돌림
        if A[start]<A[i]: # Start 값보다 커지는 순간을 찾고
            mid=i # 커지는 순간이 mid로 저장됨 -->왼쪽트리에서 오른쪽 트리로 넘어가는 순간
            break
    solve(start+1,mid-1) # start 값보다 작은 부분을 후위 순회 --> 제일 높은 레벨까지 가면 역전이 생김 그때까지 내려간다
    solve(mid,end) # start 값보다 큰 부분을 후위 순회
    print(A[start])


solve(0,len(A)-1)