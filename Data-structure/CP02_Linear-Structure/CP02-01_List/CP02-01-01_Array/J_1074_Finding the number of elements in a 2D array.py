"""
# 1074: 2차원 배열 원소 개수 구하기
입력으로 크기 n x n인 정수형 배열 A가 주어진다.
배열 A의 원소는 a_0, a_1, ..., a_n-1이다. 
입력으로 k가 주어지면 배열 A의 원소 중에서 값이 k인 원소의 개수를 출력하자.
"""

n, k = map(int, input().split()) # 
A = list(list(map(int, input().split())) for _ in range(n)) # 

# (1)
def solution(n, k, A):
    ans = 0
    for i in range(n):
        for j in range(n):
            element = A[i][j]
            if element == k:
                ans += 1
    return ans 

print(solution(n, k, A))


# code ref: joonlab(1074)