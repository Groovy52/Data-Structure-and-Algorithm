# 9095: 1, 2, 3 더하기 
T = int(input())

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for _ in range(T):
    n = int(input())
    print(dp[n])


# code ref: backjoon(9095) / 알고리즘 분류: 다이나믹 프로그래밍