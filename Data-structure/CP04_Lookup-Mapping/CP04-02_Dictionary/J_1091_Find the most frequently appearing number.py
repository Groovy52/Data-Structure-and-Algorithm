"""
1091: 가장 많이 나온 수 찾기

문제 설명
n개의 양의 정수가 저장된 배열 A가 주어진다. 배열 A에는 같은 수가 여러 개 존재할 수 있다. 
배열 A에서 출현 횟수가 가장 많은 수를 오름차순으로 출력하자.

입력 설명
첫 번째 줄에 배열 A의 크기 n이 주어진다.
두 번째 줄에 배열 A에 저장된 n개의 양의 정수가 빈칸을 사이에 두고 순서대로 주어진다.

출력 설명
첫 번째 줄에 배열 A에서 출현 횟수가 가장 많은 수를 빈칸을 사이에 두고 오름차순으로 출력한다.
"""

# 1) for 문 2번 -> 비효율적일 수 있음
n = int(input())
A = list(map(int, input().split()))

D = dict()
for a in A:
    if a not in D:
        D[a] = 1 
    else:
        D[a] += 1 

max_num = 0

for k, v in D.items():
    max_num = max(max_num, v)
    
answer = []
for k, v in D.items():
    if max_num==v:
        answer.append(k)
        
answer.sort()
print(*answer)

# 2) for문 1번으로 축약
n = int(input())
A = list(map(int, input().split()))

D = dict()
max_num = 0
for a in A:
    if a not in D:
        D[a] = 1 
    else:
        D[a] += 1 
    max_num = max(max_num, D[a])

answer = []
for k, v in D.items():
    if max_num==v:
        answer.append(k)
answer.sort()

print(*answer)


# code ref: joonlab(1091) / 알고리즘 분류: 딕셔너리, 맵, 문자열, 구현, 정렬