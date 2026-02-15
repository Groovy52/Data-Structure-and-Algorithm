"""
# 1072: 배열 단일 업데이트
크기 n인 정수형 배열 A가 주어진다. 배열 A의 원소는 a0, a1, ..., an-1이다.

입력으로 i,j,k가 주어지면 배열 A의 i번째 원소 ai부터 j번째 원소 aj에 k를 곱하는 연산을 수행하자.

연산을 수행한 후 배열 A의 모든 원소의 합을 출력하자.
"""

n = int(input())
A = list(map(int, input().split()))
i,j,k = map(int, input().split())

def solution(A, i, j, k):
    S = A[:i] + [x*k for x in A[i: j+1]] + A[j+1:]
    return sum(S)
    
print(solution(A, i, j, k))
        
        
        
# code ref: joonlab(1072) / 알고리즘 분류: 배열, 구현
