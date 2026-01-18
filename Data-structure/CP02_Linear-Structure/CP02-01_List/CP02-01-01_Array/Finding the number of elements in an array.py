"""
# 1071: 배열 원소 개수 구하기
입력으로 크기 n인 정수형 배열 A와 정수 k가 주어진다. 
배열 A의 원소는 a_0, a_1, ..., a_n-1이다. 배열 A의 원소 중에서 
값이 k인 원소의 개수를 출력하자.
"""

n, k = map(int, input().split()) # 8 7
A = list(map(int, input().split())) # 1 3 5 7 9 11 13 15

# (1)
def solution(n, A, k):
    num = 0
    for a in A:
        if a == k:
            num += 1
    return num

print(solution(n, A, k)) # 1


# (2)
from collections import Counter
def solution(n, A):
    return Counter(A)    # Counter({1: 1, 3: 1, 5: 1, 7: 1, 9: 1})

print(solution(n, A)[k]) # 1



# code ref: joonlab(1071)