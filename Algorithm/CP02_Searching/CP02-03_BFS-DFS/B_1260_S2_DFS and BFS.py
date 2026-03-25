# 1260: DFS와 BFS

# 틀린 코드: sort 정렬 문제
N, M, V = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(M)]
li.sort()

E = [[] for _ in range(N+1)]
for s, e in li:
    E[s].append(e)
    E[e].append(s)

v = [False]*(N+1)
res = []

def dfs(E, V):
    v[V] = True
    res.append(V)

    for nxt in E[V]:
        if not v[nxt]:
            dfs(E, nxt)
            
def bfs(E, V):
    from collections import deque 

    v = [False]*(N+1)
    q = deque()
    res = []
    q.append(V)
    v[V] = True

    while q:
        curr = q.popleft()
        res.append(curr)
        for nxt in E[curr]:
            if not v[nxt]:
                q.append(nxt)
                v[nxt] = True
    return res

dfs(E, V)
print(*res)
print(*bfs(E, V))


# 에러 해결
N, M, V = map(int, input().split())
E = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    E[s].append(e)
    E[e].append(s)

for e in E:
    e.sort()

v = [False]*(N+1)
res = []

def dfs(E, V):
    v[V] = True
    res.append(V)

    for nxt in E[V]:
        if not v[nxt]:
            dfs(E, nxt)
            
def bfs(E, V):
    from collections import deque 

    v = [False]*(N+1)
    q = deque()
    res = []
    q.append(V)
    v[V] = True

    while q:
        curr = q.popleft()
        res.append(curr)
        for nxt in E[curr]:
            if not v[nxt]:
                q.append(nxt)
                v[nxt] = True
    return res

dfs(E, V)
print(*res)
print(*bfs(E, V))


# 깔끔하게 작성
N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)] # 정점 번호가 1부터 시작하기 때문에, N이 아니고 N+1
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
    
for i in range(1, N+1):
    adj[i].sort()

# dfs =>
dfs_visited = [False]*(N+1)
dfs_result = []

def dfs(v):
    dfs_visited[v] = True
    dfs_result.append(v)

    for nxt in adj[v]:
        if not dfs_visited[nxt]:
            dfs(nxt)

# bfs =>
from collections import deque

bfs_visited = [False]*(N+1)
bfs_result = []

def bfs(start):
    bfs_visited[start] = True
    q = deque([start])

    while q:
        v = q.popleft()
        bfs_result.append(v)

        for nxt in adj[v]:
            if not bfs_visited[nxt]:
                bfs_visited[nxt] = True
                q.append(nxt)
                
dfs(V)
bfs(V)
print(*dfs_result)
print(*bfs_result)


# code ref: backjoon(1260) / 알고리즘 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색