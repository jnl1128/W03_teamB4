# 연산자 끼워넣기 #DFS인 이유: depth == N일 때까지 내려갔다 오니까
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
nums = list(map(int, input().split(' ')))
operators = list(map(int, input().split(' ')))
MAXRESULT = -1000000000
MINRESULT = 1000000000

def solution(depth, tmpResult):
    global MAXRESULT, MINRESULT
    if depth == N:
        MAXRESULT = max(tmpResult, MAXRESULT)
        MINRESULT = min(tmpResult, MINRESULT)
        return
    # nums[i]를 해버리면 순서가 안 지켜진다.
    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            if i == 0:
                solution(depth+1, tmpResult+nums[depth])
            elif i == 1:
                solution(depth+1, tmpResult-nums[depth])
            elif i == 2:
                solution(depth+1, tmpResult*nums[depth])
            else:
                if tmpResult < 0:
                    solution(depth+1, -(-tmpResult//nums[depth]))
                else:
                    solution(depth+1, tmpResult//nums[depth])

            operators[i] += 1

solution(1, nums[0])
print(f'{MAXRESULT}\n{MINRESULT}')