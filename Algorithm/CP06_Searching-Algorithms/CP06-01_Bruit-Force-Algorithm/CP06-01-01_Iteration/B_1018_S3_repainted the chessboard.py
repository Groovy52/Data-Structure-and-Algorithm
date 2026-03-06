# 1018: 체스판 다시 칠하기

M, N = map(int, input().split())
board = list(list(input().strip()) for _ in range(M))

def solution(M, N, board):
    # colour => left top colour; start colour
    min_count = 8*8
    for i in range(M - 7):
        for j in range(N - 7):
            
            count_w = 0
            count_b = 0

            # new 8 x 8 board =>
            for x in range(i, i+8): # x, y = 좌표
                for y in range(j, j+8):
                    if (x+y)%2 == 0:
                        if board[x][y] != 'W':
                            count_w += 1
                        else:
                            count_b += 1
                    else:
                        if board[x][y] == 'W':
                            count_w += 1
                        else:
                            count_b += 1

            min_count = min(min_count, count_w, count_b)

    return min_count

print(solution(M, N, board))
    

# code ref: backjoon(1018) / 알고리즘 분류: 구현, 브루트포스 알고리즘