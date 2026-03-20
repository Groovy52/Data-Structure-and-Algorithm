# 1764: 듣보잡

n, m = map(int, input().split())
def solution(n, m):
    dict_n = dict()
    for _ in range(n):
        not_hear = input().strip()
        dict_n[not_hear] = 1 
    answer = []
    for _ in range(m):
        not_see = input().strip()
        if not_see in dict_n:
            answer.append(not_see)

    return answer

answer = solution(n, m)
answer.sort()

print(len(answer))
for a in answer:
    print(a)

# code ref: backjoon(1764) / 알고리즘 분류: 자료구조, 문자열, 정렬, 집합과 맵, 해시를 사용한 집합과 맵