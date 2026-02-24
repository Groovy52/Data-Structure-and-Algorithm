# 1156: 피보나치 수를 동적 계획법으로

n = int(input())

def solution(n):
    if n <= 2:
        return 1 
    
    DP_table = [0] * (n + 1) # 0은 버릴 거임.
    DP_table[1] = DP_table[2] = 1 # 제일 중요한 초기 조건, 피보나치 수열 나오면 이 조건 먼저 항상 생각하기
    for i in range(3, n + 1):
        DP_table[i] = (DP_table[i-1] + DP_table[i-2]) % 987654321
    
    return DP_table[n]
    
print(solution(n))

# code ref: joonlab(1156) / 알고리즘 분류: 동적계획법