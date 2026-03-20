# 11726: 2xn 타일링

# 런타임 에러
n = int(input())
dp = [0]*(n+1)
def solution(n):
    """
    만약 n = 1이면
    dp[2]에서 인덱스 에러 발생
    """
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007
    
    return dp[n]

print(solution(n))

# 에러 고친 코드
"""
테스트케이스는 맞았는데 런타임 에러 발생할 때
문제 조건에서 주어진 입력값 범위에서 테스트해볼 수 있는 가장 최소값, 최대값 넣어서
확인해보기
=> 위 코드같은 경우 n은 1부터 1000까지 가능한데, 1이면 dp[2]에서 에러남
"""

n = int(input())

def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

    return dp[n]

print(solution(n))

# 다른 코드
n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    li = [0,1,2]
    for i in range(3,n+1):
        li.append(li[i-2]+li[i-1])
    print(li[n]%10007)


# code ref: backjoon(11726) / 알고리즘 분류: 다이나믹 프로그래밍