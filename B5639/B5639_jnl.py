# 이진 검색 트리
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

arr = []
while True:
    try:
        node = int(input())
    except:
        break
    arr.append(node)

def solution(start, end):
    # 역전이 일어나는 지점
    if start > end:
        return
    # tmp: 오른쪽 트리의 루트
    tmp = end + 1
    # arr[start]: 루트
    for i in range(start+1, end+1):
        if arr[i] > arr[start]:
            tmp = i
            break
    # tmp-1을 하는 이유는 오른쪽 트리로 넘어가지 않아야 하니까
    # start+1 : 왼쪽 트리의 새로운 루트
    solution(start+1, tmp-1)
    # tmp: 오른쪽 트리의 새로운 루트
    solution(tmp, end)

    print(arr[start])

solution(0, len(arr)-1)