# 14940: 쉬운 최단거리
n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

from collections import deque

d = [[-1] * m for _ in range(n)] # 방문처리와 거리 처리
q = deque()

for i in range(n):
    for j in range(m):
        if g[i][j] == 0:
            d[i][j] = 0
        elif g[i][j] == 2:
            q.append((i, j))
            d[i][j] = 0

dd = [[-1, 0], [1, 0], [0, -1], [0, 1]]

while q:
    r, c = q.popleft()

    for dr, dc in dd:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < n and 0 <= nc < m:
            if g[nr][nc] == 1 and d[nr][nc] == -1:
                d[nr][nc] = d[r][c] + 1
                q.append((nr, nc))

for i in range(n):
    print(*d[i])


# code ref: backjoon(14940) / 알고리즘 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 격자 그래프