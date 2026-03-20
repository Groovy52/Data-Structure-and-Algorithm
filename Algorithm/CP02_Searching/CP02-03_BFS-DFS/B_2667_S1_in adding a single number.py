# 2667: 단지번호붙이기
n = int(input())
graph = list(list(map(int, input())) for _ in range(n))

from collections import deque 

visited = [[False]*n for _ in range(n)]

def bfs(sr, sc):
    q = deque()
    q.append((sr,sc))
    visited[sr][sc] = True
    count = 1

    drc = [[-1,0],[1,0],[0,-1],[0,1]]

    while q:
        r, c = q.popleft()
        for dr, dc in drc:
            nr, nc = r+dr, c+dc 
            if 0<=nr<n and 0<=nc<n and not visited[nr][nc] and graph[nr][nc]==1:
                visited[nr][nc] = True
                q.append((nr, nc))
                count+=1
    return count

result =[]
for r in range(n):
    for c in range(n):
        if graph[r][c] == 1 and not visited[r][c]:
            result.append(bfs(r, c))

print(len(result))
result.sort()
for res in result:
    print(res)


# code ref: backjoon(2667) / 알고리즘 분류: 그래프이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색, 격자 그래프, 플러드 필