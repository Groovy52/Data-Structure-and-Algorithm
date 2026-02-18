# 1260: DFS와 BFS

N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)] # 정점 번호가 1부터 시작하기 때문에, N이 아니고 N+1
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
    
for i in range(1, N+1):
    adj[i].sort()
    
dfs_visited = [False]*(N+1)
dfs_result = []

def dfs(v):
    dfs_visited[v] = True
    dfs_result.append(v)

    for nxt in adj[v]:
        if not dfs_visited[nxt]:
            dfs(nxt)

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