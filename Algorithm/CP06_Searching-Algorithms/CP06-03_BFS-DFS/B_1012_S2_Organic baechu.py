# 1012: 유기농 배추

# 1) BFS
def bfs(sr, sc, cases, visited, N, M):
    from collections import deque
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = True 
    count = 1 

    drc = [[-1,0],[1,0],[0,-1],[0,1]]

    while q:
        r, c = q.popleft()
        for dr, dc in drc:
            nr, nc = r+dr, c+dc 
            if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and (nr, nc) in cases:
                visited[nr][nc] = True
                q.append((nr, nc))
                count+=1
    return count

T = int(input())
for _ in range(T):
    M,N,C = map(int, input().split())
    visited = [[False]*M for _ in range(N)]

    cases = []
    for _ in range(C):
        c, r = map(int, input().split())
        cases.append((r, c))
    res = []
    for sr, sc in cases:
        if not visited[sr][sc]:
            res.append(bfs(sr, sc, cases, visited, N, M))
    print(len(res))


# code ref: backjoon(1012) / 알고리즘 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색, 격자 그래프, 플러드 필