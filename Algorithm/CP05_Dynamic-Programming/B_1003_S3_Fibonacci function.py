# 1003: 피보나치 함수

# 예외처리 안 해서 인덱싱 에러
def solution(n):
    if n==0:
        return 1, 0
    dp = [[0,0] for _ in range(n+1)]
    dp[0] = [1,0]
    dp[1] = [0,1]

    for i in range(2, n+1):

        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]
        
    return dp[n][0], dp[n][1]

T = int(input())
for _ in range(T):
    n = int(input())
    print(*solution(n))

# 에러 미발생 코드
def solution(n):
    if n==0:
        return 1, 0
    dp = [[0,0] for _ in range(n+1)]
    dp[0] = [1,0]
    dp[1] = [0,1]

    for i in range(2, n+1):

        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]
        
    return dp[n][0], dp[n][1]

T = int(input())
for _ in range(T):
    n = int(input())
    print(*solution(n))

# code ref: backjoon(1003) / 알고리즘 분류: 다이나믹 프로그래밍