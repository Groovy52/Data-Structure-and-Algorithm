# 1074: Z
import sys
input = sys.stdin.readline

def z(n, r, c):
    if n == 1:
        return 2*r + c

    half = 2 ** (n - 1) # 한번 탐색 시 볼 영역
    area = half * half     # 지나온 칸 수

    # 왼쪽 위칸
    if r < half and c < half: 
        return z(n - 1, r, c)

    # 오른쪽 위칸
    elif r < half and c >= half:
        return area + z(n - 1, r, c - half) 
        

    # 왼쪽 아래칸 
    elif r >= half and c < half:
        return 2 * area + z(n - 1, r - half, c)

    # 오른쪽 아래칸
    else:
        return 3 * area + z(n - 1, r - half, c - half)

N, r, c = map(int, input().split())

print(z(N, r, c))

# 더 간단하게 구현 =>
"""
# f(n-1, r%t, c%t)
    # => 현재 좌표가 속한 작은 사분면 안에서의 방문 순서

    # t*t*(r//t*2 + c//t)
    # => 그 사분면보다 앞서 방문한 전체 칸 수
        # => r//t, c//t => 각각 0 또는 1이 나오는데,
            # r//t == 0이면 위쪽, 1이면 아래쪽
            # c//t == 0이면 왼쪽, 1이면 오른쪽

        # r//t*2 + c//t
        # => 이 식은 사분면 번호 0,1,2,3로 바꿔줌
"""
def f(n, r, c):
    if n==1:return r*2+c
    
    t=2**(n-1)
    
    return f(n-1, r%t, c%t) + t*t*(r//t*2 + c//t)

N, r, c = map(int,input().split())
print(f(N, r, c))


# code ref: backjoon(1074) / 알고리즘 분류: 분할 정복, 재귀