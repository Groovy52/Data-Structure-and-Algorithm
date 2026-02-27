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

        """
        오른쪽부터 이미 끝까지 도달한 자리들을 건너뛰고, 다음 조합을 만들기 위해 증가시킬 수 있는 자리를 찾는 과정
        가능한 한 오른쪽 자리부터 먼저 증가시켜야 사전식(lexicographic) 다음 조합이 됨.
        => ****뒤에 들어갈 숫자들이 항상 더 커야 함**** (idx[0] < idx[1] < idx[2])
        
        인덱스)
        [0,1] → [0,2] → [1,2]
        - 먼저 오른쪽(1 → 2)이 변하고
        - 오른쪽이 더 못 변할 때만 왼쪽이 변함.
        """
        move_pos = k - 1 # 오른쪽 끝 값 인덱스 초기값(나중 계속 변함) = 오른쪽 끝 자리부터 검사 시작하겠다
        """
        | 자리(i) | 최대값 = (n-k)+i = (7-3)+i |
        | -----  | ------------------------- |
        | 0      | 4                         |
        | 1      | 5                         |
        | 2      | 6                         |

        """
        while move_pos >= 0 and idx[move_pos] == (n-k) + move_pos: # idx[k-1]==n-1
            """
            왜 (n-k)+move_pos 인가?
            1) i번째 칸을 정할 때 항상 뒤에 (k-i-1)개를 남겨야 한다 => 그래야 전체 k개를 채울 수 있음
            2) 최대값 = (n-1) - (뒤에 남길 개수) = (n-1) - (k-i-1) = n-k+i
            """
            move_pos -= 1 # 오른쪽 끝 값을 더 이상 증가시킬 수 없으므로 끝 값 감소시킴

        if move_pos < 0: # 위 while 문 조건의 종료 조건
            break

        idx[move_pos] += 1 # 만들어질 문자의 오른쪽 끝값 인덱스 1 증가

        for i in range(move_pos + 1, k):
            idx[i] = idx[i - 1] + 1

    result.sort()
    return result


# code ref: joonlab(1114) / 알고리즘 분류: 구현, 완전탐색, 문자열