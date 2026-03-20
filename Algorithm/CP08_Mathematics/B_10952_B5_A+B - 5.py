# 10952: A+B - 5
"""
입력 횟수가 정해져있지 않을 때 코드 작성 방법 => 특정 조건이 종료 조건인 문제
(EOF 방식 아님)

"""

while True:
    A, B = map(int, input().split())
    if A==0 or B==0: break
    else: print(A+B)       


## code ref: backjoon(10952) / 알고리즘 분류: 수학, 구현, 사칙연산