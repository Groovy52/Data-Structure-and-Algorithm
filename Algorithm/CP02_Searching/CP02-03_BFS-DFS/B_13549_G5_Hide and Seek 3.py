# 13549: 숨바꼭질 3

# 틀린 코드 : 오류 원인 2개
from collections import deque 

def solution(N, K):
    maxtlen = 1000001
    t = [-1]*maxtlen
    q = deque()
    q.append(N)
    t[N] = 0

    while q:
        x = q.popleft()
        if x==K:
            return t[x]
        for y in (x-1, x+1, 2*x):
            # 오류 원인 1: 조건 검사 순서
            """
            파이선이 왼쪽부터 평가하므로, y 범위 검사를 먼저 안 하면
            t[y]에서 IndexError 발생
            """
            if t[y] == -1 and 0<=y<maxtlen:
                # 오류 원인 2: 이동 비용(가중치)이 다름 => x-1, x+1이면 1초 걸리고, 2*x는 0초 걸림
                """
                0초 이동이 1초 이동보다 먼저 처리된다는 보장이 없어서 최단 시간이 틀릴 수 있으므로
                비용 0 이동이면 appendleft
                비용 1 이동이면 append
                => 이렇게하면 현재까지 가장 작은 시간 순서대로 탐색됨.
                """
                q.append(y)
                if y==2*x:
                    t[y] = t[x]
                else:
                    t[y] = t[x] + 1


N, K = map(int, input().split()) 
print(solution(N, K))


# 맞긴 했지만 부정확
from collections import deque 

def solution(N, K):
    maxtlen = 1000001
    t = [-1]*maxtlen
    q = deque()
    q.append(N)
    t[N] = 0

    while q:
        x = q.popleft()
        if x==K:
            return t[x]
        for y in (x-1, x+1, 2*x):
            # 오류 해결 1: 조건 검사 순서
            if 0<=y<maxtlen and t[y] == -1:
                # 오류 해결 2: 이동 비용(가중치)이 다름 => x-1, x+1이면 1초 걸리고, 2*x는 0초 걸림
                """
                하지만 if y==2*x는 결국 값만 보고 처리되는 것이므로, 간선의 경우의 수대로 처리된다고 보장할 수 없음
                따라서 경우의 수를 아예 분리하는 것이 안전함.
                """
                if y==2*x:
                    t[y] = t[x]
                    q.appendleft(y)
                else:
                    t[y] = t[x] + 1
                    q.append(y)


N, K = map(int, input().split()) 
print(solution(N, K))


# 가장 정확한 코드
from collections import deque 

def solution(N, K):
    maxtlen = 1000001
    t = [-1]*maxtlen
    q = deque()
    q.append(N)
    t[N] = 0

    while q:
        x = q.popleft()
        if x==K:
            return t[x]
        
        y = 2*x 
        if 0<=y<maxtlen and t[y] == -1:
            t[y] = t[x]
            q.appendleft(y)
        
        for y in (x-1, x+1):
            if 0<=y<maxtlen and t[y] == -1:
                t[y] = t[x] + 1
                q.append(y)


N, K = map(int, input().split()) 
print(solution(N, K))


# code ref: backjoon(13549) / 알고리즘 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 최단 경로, 데이크스트라, 0-1 너비 우선 탐색