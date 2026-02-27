# 1117: 정수를 거꾸로 출력하기

# 재귀
import sys
sys.setrecursionlimit(10**6)

A = int(input())

def solution(A, B):
    if A > 0:
        if A%10 != 0 or B == 1:
            print(A%10, end = '')
            B = 1
        
        solution(A//10, B)

solution(A, 0)

# 반복문
import sys
sys.setrecursionlimit(10**6)

A = int(input())

def solution(A):
    B = 0
    while A > 0:
        if A%10 != 0 or B == 1:
            print(A%10, end='')
            B = 1
        
        A //= 10

solution(A)


# code ref: joonlab(1117) / 알고리즘 분류: 완전탐색, 재귀