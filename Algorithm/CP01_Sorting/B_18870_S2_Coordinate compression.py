# 18870: 좌표 압축

"""
문제의 출력 결과 의미
= Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수
=> Xi, Xj모두 인풋 리스트에 있는 값으로 현재 인덱스의 값 Xi가 나머지 원소 Xj보다 큰 경우는 몇개인가?
=> 즉, Xi보다 작은 원소들의 개수 Xj가 몇개인가?
"""
# 시간 초과 발생 (이유: solution을 N번 반복)
import sys 
input = sys.stdin.readline 

def solution(arr):
    sorted_unique = sorted(set(arr)) # = sorted(unique())
    compressed = dict()
    for i, v in enumerate(sorted_unique):
        compressed[v] = i 

    return compressed 

N = int(input())
coords = list(map(int, input().split()))
for c in coords:
    print(solution(coords)[c], end = ' ')

# 오류 해결
import sys 
input = sys.stdin.readline 

def solution(arr):
    sorted_unique = sorted(set(arr)) # = sorted(unique())
    compressed = dict()
    for i, v in enumerate(sorted_unique):
        compressed[v] = i 

    return compressed 

N = int(input())
coords = list(map(int, input().split()))
ans = solution(coords)

for c in coords:
    print(ans[c], end = ' ')
    # print(*[result[c] for c in coords])
    # print(' '.join(map(str, [result[c] for c in coords])))



# code ref: backjoon(18870) / 알고리즘 분류: 정렬 / 값/좌표압축