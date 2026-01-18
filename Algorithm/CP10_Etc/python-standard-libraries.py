# -----------------------------
#   combinations 함수 예제 (from itertools)
# -----------------------------

"""
combinations 함수 설명:
- itertools.combinations(iterable, r)
    -> iterable에서 r개의 요소를 선택하는 **모든 조합(combination)**을 반환
- 문자열 A에 대해 조합 C(A, k)를 생성할 때:
    문자열 A에 있는 문자 중 임의로 k개를 선택하여, 문자열 A에서의 순서를 유지하여 만든 모든 부분 수열을 모아야 한다.
    즉:
        combinations(A, k)는 문자열 A의 문자 순서를 유지하는 조합을 자동으로 만들어준다.
- 순서를 고려하지 않음 (즉, (A, B)와 (B, A)는 같은 것으로 간주)
- 예를 들어 A = 'cba'일 때, combinations('cba', 2)는 ('c', 'b'), ('c', 'a'), ('b', 'a') 를 생성한다.
- 입력값: 문자열 / 출력값: 튜플(tuple)
"""

# 문자열에서 2개 문자 선택해 조합 생성
from itertools import combinations

s= 'abc'
b = combinations(s, 2)
for i in b:
    print(i)
    
# 출력
# ('a', 'b')
# ('a', 'c')
# ('b', 'c')


# -----------------------------
#   permutations 함수 예제 (from itertools)
# -----------------------------

"""
permutations 함수 설명:
- itertools.permutations(iterable, r)
    -> iterable에서 r개의 요소를 **순열(permutation)**로 나열한 모든 경우의 수를 반환
- 반환 결과는 튜플(tuple)의 형태
- r 생략 시: iterable 전체 길이만큼의 순열 생성
- 순서가 다르면 다른 것으로 간주 (즉, ('a', 'b') ≠ ('b', 'a'))
"""

from itertools import permutations

# 기본 예제
items = ['a', 'b', 'c']


# 2개씩 뽑는 모든 순열
result1 = list(permutations(items, 2))
print(result1) # [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]


# 전체 길이만큼 순열 (3!)
result2 = list(permutations(items))
print(result2) # [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

# 수 -> 문자열
N = 4; M = 2
num_list = [str(s) for s in list(range(1, N+1))]
for i in permutations(num_list, M):
    print(' '.join(i))
# 출력
# 1 2
# 1 3
# 1 4
# 2 1
# 2 3
# 2 4
# 3 1
# 3 2
# 3 4
# 4 1
# 4 2
# 4 3
