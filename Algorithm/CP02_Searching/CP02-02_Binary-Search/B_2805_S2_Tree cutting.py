# 2805: 나무 자르기

import sys
input = sys.stdin.readline

def solution(n, m, hs):
    minh = 0
    maxh = max(hs) - 1
    cuth = 0 # answer
    
    while minh <= maxh:
        midh = (minh + maxh) // 2 # 1

        get = 0
        for h in hs:
            if h > midh:
                get += h-midh
        
        if get >= m:
            cuth = midh
            minh = midh + 1 # 2
        else:
            maxh = midh - 1 # 3

    return cuth

N, M = map(int, input().split())
heights = list(map(int, input().split()))
print(solution(N, M, heights))


# code ref: backjoon(2805) / 알고리즘 분류: 이분 탐색, 매개 변수 탐색