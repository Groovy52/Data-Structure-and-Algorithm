# 25417: 고속의 숫자 탐색

board = list(list(map(int, input().split())) for _ in range(5))
sr, sc = map(int, input().split())

from collections import deque

def solution(board, sr, sc):
    for r in range(5):
        for c in range(5):
            if board[r][c] == 1:
                return get_move_cnt(board, sr, sc, r, c)

def slide(board, r, c, dr, dc):
    cr, cc = r, c

    while True:
        nr = cr + dr
        nc = cc + dc 

        # 다음 칸 막히면 현재 칸 cr, cc에서 stop
        if not (0<=nr<5 and 0<=nc<5):
            return cr, cc 
        
        if board[nr][nc] == -1:
            return cr, cc
        
        # 7 만나면 전진한 칸에서 stop
        if board[nr][nc] == 7:
            return nr, nc

        # 범위도 안 벗어나고 -1도, 7도 안 만나면 한칸 전진
        cr, cc = nr, nc

def get_move_cnt(board, sr, sc, tr, tc):
    dist = [[0]*5 for _ in range(5)]
    dd = [[-1,0],[1,0],[0,-1],[0,1]]
    visited = [[False]*5 for _ in range(5)]

    q = deque()
    q.append([sr, sc])
    visited[sr][sc] = True

    while q:
        cr, cc = q.popleft()
        if cr==tr and cc==tc:
            return dist[cr][cc]

        for dr, dc in dd:
            # 걸을 때
            nr, nc = cr+dr, cc+dc
            if 0<=nr<5 and 0<=nc<5 and board[nr][nc] != -1 and not visited[nr][nc]:
                visited[nr][nc] = True
                dist[nr][nc] = dist[cr][cc] + 1
                q.append([nr, nc])

            # 뛸 때
            nr, nc = slide(board, cr, cc, dr, dc)
            if not visited[nr][nc]:
                visited[nr][nc] = True
                dist[nr][nc] = dist[cr][cc] + 1
                q.append([nr, nc])
    
    return -1


print(solution(board, sr, sc))


# code ref: joonlab(1541) / backjoon(25417) / 알고리즘 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색