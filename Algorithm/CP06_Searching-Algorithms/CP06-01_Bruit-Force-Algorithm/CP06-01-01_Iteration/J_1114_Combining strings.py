# 1114: 문자열 조합하기

# 1) 조합 함수 사용: from iterools import combinations
A = input().strip()
k = int(input())

from itertools import combinations
def solution(A, k):
    return sorted([''.join(a) for a in list(combinations(A, k))])

for a in solution(A, k):
    print(a)

# 2) python 내장 함수 사용하지 않고 반복문으로만 구현 =>
A = input().strip()
k = int(input())

def solution(A, k):
    n = len(A)
    idx = list(range(k))

    result = []

    while True:
        comb = ''
        for i in range(k):
            comb += A[idx[i]]
        result.append(comb)

        move_pos = k - 1
        while move_pos >= 0 and idx[move_pos] == (n-k) + move_pos:
            move_pos -= 1

        if move_pos < 0:
            break

        idx[move_pos] += 1

        for i in range(move_pos + 1, k):
            idx[i] = idx[i - 1] + 1

    result.sort()
    return result


# code ref: joonlab(1114) / 알고리즘 분류: 구현, 완전탐색, 문자열
