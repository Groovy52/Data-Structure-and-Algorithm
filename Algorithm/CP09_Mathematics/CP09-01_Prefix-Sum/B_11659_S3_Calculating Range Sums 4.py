# 11659: 구간 합 구하기 4

# 시간초과 발생
"""
알고리즘 상에서 시간초과 오류가 없어도 입출력 수 자체가 많은 경우 
그냥 input()으로 받으면 시간초과 오류가 발생할 수 있다.

ex. 문제조건: 
첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다
1 ≤ N ≤ 100,000
1 ≤ M ≤ 100,000

"""
n, m = map(int, input().split())
A = list(map(int, input().split()))
P = [0] * n
P[0] = A[0]
for idx in range(1, n):
    P[idx] = P[idx-1] + A[idx]

for _ in range(m):
    i, j = map(int, input().split())
    s, e = i-1, j-1
    if s==0:
        print(P[e])
    else:
        print(P[e] - P[s - 1])

# 에러 고친 코드
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

P = [0] * n
P[0] = A[0]
for idx in range(1, n):
    P[idx] = P[idx - 1] + A[idx]

res = []
for _ in range(m):
    i, j = map(int, input().split())
    s, e = i - 1, j - 1
    if s == 0:
        res.append(str(P[e]))
    else:
        res.append(str(P[e] - P[s - 1]))

sys.stdout.write('\n'.join(res))


# code ref: backjoon(11659) / 알고리즘 분류: 누적 합