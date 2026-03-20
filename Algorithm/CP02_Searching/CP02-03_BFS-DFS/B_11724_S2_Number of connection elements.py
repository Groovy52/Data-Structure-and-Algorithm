# 11724: 연결 요소의 개수

# 시간 초과 발생 코드
N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

def bfs(cur, visited):
    from collections import deque 
    q = deque()
    q.append(cur)
    visited[cur] = True 
    count = 1
    while q:
        u = q.popleft()
        for v in edges[u]:
            if not visited[v]:
                q.append(v)
                visited[v] = True
                count +=1 
    return count

res = []
visited = [False]*(N+1)
for i in range(1,N+1):
    if not visited[i]:
        res.append(bfs(i, visited))

print(len(res))

# 에러 고친 코드
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

def bfs(cur, visited):
    from collections import deque 
    q = deque()
    q.append(cur)
    visited[cur] = True 

    while q:
        u = q.popleft()
        for v in edges[u]:
            if not visited[v]:
                q.append(v)
                visited[v] = True

count = 0 # 이 변경 부분은 에러와 큰 상관 없음
visited = [False]*(N+1)
for i in range(1,N+1):
    if not visited[i]:
        bfs(i, visited)
        count += 1

print(count)

# code ref: backjoon(11724) / 알고리즘 분류: 