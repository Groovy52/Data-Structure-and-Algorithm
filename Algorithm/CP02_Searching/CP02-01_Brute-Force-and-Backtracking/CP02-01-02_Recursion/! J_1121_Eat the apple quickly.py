# 1121: 사과 빨리 먹기

board = list(list(map(int, input().split())) for _ in range(5))
r, c = map(int, input().split())

def solve(board, r, c, have_to_eat):
    if have_to_eat == 0:
        return 0 
    
    ret = -1 # 사과 3개를 먹을 수 없는 경우 

    dd = [[-1,0],[1,0],[0,-1],[0,1]]
    for dr, dc in dd:
        nr, nc = r+dr, c+dc
        if 0<=nr<5 and 0<=nc<5 and board[nr][nc] != -1:
            prv_value = board[r][c]
            board[r][c] = -1

            cur_ret = solve(board, nr, nc, have_to_eat - board[nr][nc])

            if cur_ret != -1:
                cur_ret += 1 

            if cur_ret != -1:
                if ret == -1 or cur_ret < ret:
                    ret = cur_ret
            
            board[r][c] = prv_value
            
    return ret 

print(solve(board, r, c, 3))


# code ref: joonlab(1121) / 알고리즘 분류: 완전탐색, 구현, 재귀, 백트래킹