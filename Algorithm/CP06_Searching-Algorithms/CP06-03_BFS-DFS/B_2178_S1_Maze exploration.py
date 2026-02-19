# 2178: 미로 탐색

N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, input())))

def solution(N, M, maze):
    from collections import deque
    q = deque()
    visited = [[False]*M for _ in range(N)]
    dist = [[0]*M for _ in range(N)]

    cr, cc = 0, 0
    q.append([cr, cc])
    visited[cr][cc] = True 
    dist[cr][cc] = 1

    tr, tc = N-1, M-1
    while q:
        cr, cc = q.popleft()
        if cr==tr and cc==tc:
            return dist[cr][cc]
        
        dd = [[-1,0],[1,0],[0,-1],[0,1]]
        for dr, dc in dd:
            nr, nc = cr+dr, cc+dc
            if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and maze[nr][nc]!=0:
                q.append([nr, nc])
                visited[nr][nc] = True 
                dist[nr][nc] = dist[cr][cc] + 1
                
print(solution(N, M, maze))

# code ref: backjoon(2178) / 알고리즘 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 격자 그래프