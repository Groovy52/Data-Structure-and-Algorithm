# 1156: 피보나치 수를 동적 계획법으로

n = int(input())

def solution(n):
    if n <= 2:
        return 1 
    dp_table = [0] * (n + 1)
    dp_table[1] = dp_table[2] = 1
    for i in range(3, n + 1):
        dp_table[i] = (dp_table[i-1]+dp_table[i-2]) % 987654321

    return dp_table[n]
    
print(solution(n))


# code ref: joonlab(1156) / 알고리즘 분류: 동적계획법