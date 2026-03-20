# 15650: N과 M (2)

N, M = map(int, input().split())

from itertools import combinations

comb = combinations(list(range(1, N+1)), M)
for c in comb:
    print(*c)


# code ref: backjoon(15650) / 알고리즘 분류: 백트랙킹