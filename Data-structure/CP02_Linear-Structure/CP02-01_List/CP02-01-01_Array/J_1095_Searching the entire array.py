"""
1095: 배열 전체 탐색하기

문제 설명
크기 n인 정수형 배열 A가 주어진다. 배열 A의 원소는 A[0],A[1],...,A[n-1]이다. 
배열 A에는 같은 값을 갖는 원소가 여러 개 존재할 수 있다. 배열 A에 대한 m개의 질의가 
저장된 배열 B가 주어진다. 배열 B에 저장된 m개의 질의는 아래와 같은 유형이다.

- k : 배열 A의 원소 중 k보다 크거나 같은 원소의 개수를 출력한다.
배열 B에 저장된 첫 번째 질의부터 m번째 질의까지 순서대로 처리하면서 질의 결과를 출력하자.
"""
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(int(input()) for _ in range(m))

def solution(n, m, A, B):
    for k in B:
        print(len([x for x in A if x >= k]))

solution(n, m, A, B)


# code ref: joonlab(1095) / 알고리즘 분류: 배열, 구현