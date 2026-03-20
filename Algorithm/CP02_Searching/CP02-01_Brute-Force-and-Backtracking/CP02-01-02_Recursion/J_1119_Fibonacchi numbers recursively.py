# 1119: 피보나치 수를 재귀로

import sys 
sys.setrecursionlimit(10**6)


n = int(input())
def f(N):
    if N <=2:
        return 1 
    else:
        return f(N-1) + f(N-2)

print(f(n))

# code ref: joonlab(1119) / 알고리즘 분류: 완전탐색, 구현, 재귀