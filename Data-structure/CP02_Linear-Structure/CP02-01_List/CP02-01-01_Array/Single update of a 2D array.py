"""
# 1075: 2차원 배열 단일 업데이트
크기가 n x n인 정수형 2차원 배열 A가 주어진다. 
배열 A의 원소는 a0, a1, ..., an-1이다. 
aij에서 i가 행 번호, j가 열 번호이다.

입력으로 i1,j1,i2,j2,k 가 주어지면 행 번호가 i1~i2이고 열 번호가 j1~j2 인 배열
A의 모든 원소에 k를 곱하는 연산을 수행한다. 
연산을 수행한 후 배열 A의 모든 원소의 합을 출력하자.

"""

n = int(input())
A = list(list(map(int, input().split())) for _ in range(n))
i1, j1, i2, j2, k = map(int, input().split())

def solution(n, A, i1, j1, i2, j2, k):
    for i in range(i1, i2+1):
        for j in range(j1, j2+1):
            A[i][j] *= k
    
    ans = 0
    for a in A:
        ans += sum(a)
    return ans
    
print(solution(n, A, i1, j1, i2, j2, k))


# code ref: joonlab(1075) / 알고리즘 분류: 배열, 제어문, 구현
