# 5430: AC

# 틀린 코드
"""
틀린 원인:
이 코드는 리스트를 실제로 뒤집고, 맨 앞 원소를 직접 삭제하는 방식으로 구현했기 때문에 시간초과가 발생함.

1) numbers.reverse()
- R이 나올 때마다 리스트 전체를 뒤집고 있음
- 리스트 길이가 n일 때 reverse()는 O(n)
- 함수 문자열 p의 길이는 최소 1에서 100,000 = 10**5 이하임,
    시간복잡도 1초 면 10**8 이상이면 보통 백준 기준 에러 발생(확실 x), 
    R이 많이 나오면 전체 시간 복잡도가 커짐

2) numbers.pop(0)
- 파이썬 리스트에서 맨 앞 원소 삭제는 O(n)
- 이유: 뒤에 있는 모든 원소를 한 칸씩 앞으로 당겨야 하기 때문
- D가 여러 번 나오면 이 연산이 반복되어 매우 비효율적임

즉, 이 문제는 R을 만날 때마다 실제로 뒤집지 말고, 
R이 있으면 D가 나왔을 때 뒤에서 빼고, R 없으면 앞에서 빼면 됨.

또한 D 연산도 리스트의 pop(0)으로 처리하면 안 되고,
앞/뒤 삭제가 모두 빠른 자료구조를 사용해야 함.

핵심 원리:
- R: 실제 reverse() 하지 말고 방향 상태만 토글
- D: 현재 방향에 따라 앞 또는 뒤에서 삭제
- 따라서 deque 같은 자료구조를 써야 효율적으로 해결 가능
"""

def solution(numbers, functions):
    for func in functions:
        if func == 'R':
            numbers.reverse()
        else:
            if not numbers:
                return 'error'
            numbers.pop(0)

    return numbers


import ast

T = int(input())
for _ in range(T):
    functions = input().strip()
    n = int(input())
    arr = ast.literal_eval(input().strip())
    print(solution(arr, functions))


# 개선 코드
from collections import deque
import sys

input = sys.stdin.readline # 혹시 모를 시간초과를 위해 작성하는 것이 안전

T = int(input())

for _ in range(T):
    p = input().strip()
    n = int(input())
    arr_str = input().strip()

    if n == 0:
        arr = deque()
    else:
        arr = deque(map(int, arr_str[1:-1].split(',')))

    reversed_flag = False
    error = False

    for cmd in p:
        if cmd == 'R':
            reversed_flag = not reversed_flag
        else:  # cmd == 'D'
            if not arr:
                print("error")
                error = True
                break

            if not reversed_flag:
                arr.popleft()
            else:
                arr.pop()

    if not error:
        if reversed_flag:
            arr.reverse()
        print('[' + ','.join(map(str, arr)) + ']')