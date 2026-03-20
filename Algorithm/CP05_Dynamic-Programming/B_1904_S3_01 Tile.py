# 1904: 01 타일

N = int(input())

dp = [0]*(N+1)

for i in range(1, N+1):
    if i<=2:
        dp[i] = i
    else:
        dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[N])

# 자주 하는 실수
dp = [0]*(N+1)
dp[1] = 1 
dp[2] = 2  # dp = [0]*(N+1) 줄로 인해 인덱스 에러

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])


# code ref: backjoon(1904) / 알고리즘 분류: 동적 계획법