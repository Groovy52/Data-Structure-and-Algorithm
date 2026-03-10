# 1463: 1로 만들기

# 틀린 코드: 각 조건문이 서로 독립되지 않은 상태에서 if, elif 로 작성하면 모든 조건 검사 못함
n = int(input())

def solution(n):
    dp = [0]*(n+1)
    if n==1:
        return 0
    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1
        if i%3==0:
            dp[i] = min(dp[i], dp[i//3]+1)
        elif i%2==0:
            dp[i] = min(dp[i], dp[i//2]+1)
        elif i%2==0 and i%3==0:
            dp[i] = min(dp[i], dp[i//2]+1, dp[i//3]+1)
    return dp[n]

print(solution(n))

# 에러 미발생 코드
n = int(input())

def solution(n):
    dp = [0]*(n+1)
    if n==1:
        return 0
    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1
        if i%3==0:
            dp[i] = min(dp[i], dp[i//3]+1)
        if i%2==0:
            dp[i] = min(dp[i], dp[i//2]+1)
    return dp[n]

print(solution(n))

# code ref: backjoon(1463) / 알고리즘 분류: 다이나믹 프로그래밍