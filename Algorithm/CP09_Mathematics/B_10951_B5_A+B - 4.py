# 10951: A+B - 4
"""
입력 횟수가 정해져있지 않을 때 코드 작성 방법 => EOF 방식

"""

# 1)
import sys

for line in sys.stdin:
    A, B = map(int, line.split())
    print(A+B)

# 2)
while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except:
        break


## code ref: backjoon(10951) / 알고리즘 분류: 수학, 구현, 사칙연산