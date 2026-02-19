# 1533: 빠른 숫자 탐색

from collections import deque 

def get_move_cnt(board, sr, sc, tr, tc):
    dd = [[-1,0], [1,0],[0,-1],[0,1]]
    visited = [[False]*5 for _ in range(5)] 
    dist = [[0]*5 for _ in range(5)] 

    q = deque()
    q.append([sr, sc])
    visited[sr][sc] = True
    dist[sr][sc] = 0

    while q:
        cr, cc = q.popleft()
        if cr==tr and cc==tc:
            return dist[cr][cc]
    
        for dr, dc in dd:
            nr, nc = cr+dr, cc+dc
            if 0<=nr<5 and 0<=nc<5 and not visited[nr][nc] and board[nr][nc]!=-1:
                q.append([nr, nc])
                dist[nr][nc] = dist[cr][cc] + 1 
                visited[nr][nc] = True 
    
    return -1 

board = list(list(map(int, input().split())) for _ in range(5))
sr, sc = map(int, input().split())

tr, tc = 0,0 # 1이 적혀있는 칸의 행, 열 번호 = target
for r in range(5):
    for c in range(5):
        if board[r][c] == 1:
            tr, tc = r, c
            
print(get_move_cnt(board, sr, sc, tr, tc))

# code ref: joonlab(1533) / Backjoon(25416) / 알고리즘 분류: 그래프이론, 그래프탐색, 너비우선탐색