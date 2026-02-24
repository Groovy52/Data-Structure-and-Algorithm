# 25418: 정수 a를 k로 만들기

A, K = map(int, input().split())

def solution(A, K):
    dp = [0]*(K+1)
    for i in range(A+1, K+1):
        dp[i] = dp[i-1] + 1
        if i%2 == 0 and i//2 >= A:
            dp[i] = min(dp[i], dp[i//2] + 1)
    return dp[K]

print(solution(A, K))


# code ref: backjoon(25418) / joonlab(1562) / 알고리즘 분류: 동적계획법, 그래프 이론, 그래프 탐색, 너비 우선 탐색, 그리디