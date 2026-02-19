# 25513: 빠른 오름차순 숫자 탐색

board = list(list(map(int, input().split())) for _ in range(5))
sr, sc = map(int, input().split())

from collections import deque

def solution(board, sr, sc):
    target_rc = []
    answer = 0

    for i in range(1, 6+1):
        for r in range(5):
            for c in range(5):
                if board[r][c] == i:
                    target_rc.append([r,c])
    
    r, c = sr, sc
    for tr, tc in target_rc:
        ans = get_move_cnt(board, r, c, tr, tc)
        if ans == -1:
            return -1 
        else:
            answer += ans
            r,c = tr, tc

    return answer

def get_move_cnt(board, sr, sc, tr, tc):
    dist = [[0]*5 for _ in range(5)]
    dd = [[-1,0],[1,0],[0,-1],[0,1]]
    visited = [[False]*5 for _ in range(5)]
    q = deque()
    q.append([sr, sc])
    """
    1,2,3,4,5,6이 적혀 있는 칸을 여러 번 방문할 수 있다

    이건 경로 전체에서 같은 칸을 다시 지나가도 된다는 뜻이지,
    한 번의 BFS 탐색 중에 무한히 왕복해도 된다는 뜻이 절대 아님.

    Ex) visited 없이 BFS 돌리면 A → B → A → B → A → B → A → B → ...
    => 같은 거리 레벨에서 무한 왕복함.

    & visited 안 쓰는 BFS는 존재하지 않음.
    """
    visited[sr][sc] = True

    while q:
        cr, cc = q.popleft()
        if cr==tr and cc==tc:
            return dist[cr][cc]

        for dr, dc in dd:
            nr, nc = cr+dr, cc+dc 
            if 0<=nr<5 and 0<=nc<5 and not visited[nr][nc] and board[nr][nc] != -1:
                q.append([nr, nc])
                visited[nr][nc] = True
                dist[nr][nc] = dist[cr][cc] + 1
    
    return -1

print(solution(board, sr, sc))



# code ref: joonlab(1540) / backjoon(25513) / 알고리즘 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색