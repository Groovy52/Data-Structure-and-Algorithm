"""
1099: 2차원 배열 다중 업데이트 다중 합 (Small)

문제 설명
크기가 n x n인 정수형 2차원 배열 A가 주어진다. 배열 A의 원소는 A[0][0], A[0][1], …, A[n - 1][n - 1]이다. 
배열 A의 모든 원소의 초깃값은 입력으로 주어진다. 배열 A에 대한 m개의 질의가 저장된 배열 B가 주어진다. 배열 B에 저장된 m개의 질의는 아래 두 가지 유형으로 구분된다. 
첫 번째가 유형 1을 나타내고 두 번째가 유형 2를 나타낸다.

- 1 i1 j1 i2 j2 k : 행 번호 i가 i1 ≤ i ≤ i2이고, 열 번호 j가 j1 ≤ j ≤ j2인 A[i][j]에 k를 더한다.
- 2 i1 j1 i2 j2 : 행 번호 i가 i1 ≤ i ≤ i2이고, 열 번호 j가 j1 ≤ j ≤ j2인 A[i][j]의 합을 출력한다.
배열 B에 저장된 첫 번째 질의부터 m번째 질의까지 순서대로 처리하면서 유형 2에 대한 결과를 출력하자.
"""
n, m = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(n))
B = list(list(map(int, input().split())) for _ in range(m))

def solution(n, m, A, B):
    for info in B:
        if info[0] == 1:
            i1, j1, i2, j2, k = info[1:]
            for i in range(i1, i2+1):
                for j in range(j1, j2+1):
                    A[i][j] += k
        else:
            i1, j1, i2, j2 = info[1:]
            ans = 0
            for i in range(i1, i2+1):
                for j in range(j1, j2+1):
                    ans += A[i][j]
            print(ans)     
            
solution(n, m, A, B)

# code ref: joonlab(1099) / 알고리즘 분류: 배열, 구현