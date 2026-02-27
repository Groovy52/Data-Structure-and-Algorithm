# 15649: N과 M (1)

from itertools import permutations
N, M = map(int, input().split())

num_list = list(range(1, N+1))
permut = list(permutations(num_list, M))
permut.sort()
for p in permut:
    print(*p)


# code ref: backjoon(15649) / 알고리즘 분류: 백트랙킹