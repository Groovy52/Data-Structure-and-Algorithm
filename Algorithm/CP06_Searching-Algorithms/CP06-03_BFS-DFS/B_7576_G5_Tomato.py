# 7576: 토마토
M, N = map(int, input().split())
box = list(list(map(int, input().split())) for _ in range(N))

from collections import deque 

def bfs(graph, visited):
    
    q = deque()
    day = [[0]*M for _ in range(N)]
    # 처음부터 익은 토마토(1)들을 모두 큐에 넣기
    """
    밖에서 1인 r, c값 저장 후 for문 돌려 bfs 함수에 sr, sc로 입력받아 하지않고, 
    위와 같이 함수 내에서 한꺼번에 q에 넣어주는 이유는 문제 조건 때문!
    문제를 읽어보면 1인 토마토가 양 끝에 있을 때 양쪽에서 동시에 퍼졌을 때 최소 일수를 구하기 때문
    그러려면 동일 레벨에서 처리, 즉 같이 퍼져나가야 함.
    밖에서 for문 돌리면 같이 퍼져나갈 수 없음!
    """
    for r in range(N):
        for c in range(M):
            if graph[r][c] == 1:
                q.append((r, c))
                visited[r][c] = True
                day[r][c] = 0

    drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while q:
        r, c = q.popleft()
        for dr, dc in drc:
            nr, nc = r + dr, c + dc 
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and graph[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = True 
                graph[nr][nc] = 1
                day[nr][nc] = day[r][c] + 1 # count가 아니라, 이동 직전 위치를 기준으로 증가한 거리가 곧 일수(number of day)가 됨.

    # bfs 다 끝나서 q에는 값이 없는데, 0이 남아 있으면 다 못 익은 것
    for row in graph:
        if 0 in row:
            return -1 
        
    # day중 가장 큰 값이 마지막으로 익은 날짜, 다 익기까지 걸린 최소 일수임.
    max_day = 0
    for r in range(N):
        for c in range(M):
            max_day = max(max_day, day[r][c])
    
    return max_day 

boxcop = box.copy()

visited = [[False]*M for _ in range(N)]

if not any(0 in row for row in boxcop):
    print(0)
else:
    print(bfs(boxcop, visited))


# code ref: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 최단 경로, 격자 그래프