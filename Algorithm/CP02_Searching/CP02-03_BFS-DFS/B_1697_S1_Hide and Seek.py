# 1697: 숨바꼭질

# 값의 범위를 잘못 생각
from collections import deque 

def solution(s, e):
    maxt = 100000   # 걸린 시간 초기값!!!!

    visited = [-1]*maxt # 방문 여부, []위치까지 걸린 시간
    q = deque()
    
    q.append(s)
    visited[s] = 0 # 시작위치에서 시작위치까지 걸린 시간은 0이므로 0저장

    while q:
        x = q.popleft()
        if x == e:
            return visited[x]
        
        for nx in (x-1, x+1, 2*x):
            if 0 <= nx < maxt and visited[nx]==-1:
                visited[nx] = visited[x] + 1
                q.append(nx)
                
N, K = map(int, input().split())
print(solution(N, K))

# 해결
from collections import deque 

def solution(s, e):
    maxt = 100001   # 0~ 100000 !수정한 부분

    visited = [-1]*maxt # 방문 여부, []위치까지 걸린 시간
    q = deque()
    
    q.append(s)
    visited[s] = 0 # 시작위치에서 시작위치까지 걸린 시간은 0이므로 0저장

    while q:
        x = q.popleft()
        if x == e:
            return visited[x]
        
        for nx in (x-1, x+1, 2*x):
            if 0 <= nx < maxt and visited[nx]==-1:
                visited[nx] = visited[x] + 1
                q.append(nx)
                
N, K = map(int, input().split())
print(solution(N, K))


# code ref: backjoon(1697) / 알고리즘 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색