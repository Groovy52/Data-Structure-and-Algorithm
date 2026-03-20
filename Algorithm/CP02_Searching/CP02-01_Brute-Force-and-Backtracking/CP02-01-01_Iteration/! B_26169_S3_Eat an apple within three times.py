# 26169: 세 번 이내에 사과를 먹자

# 1) 3중 반복문으로
board = list(list(map(int, input().split())) for _ in range(5))
r, c = map(int, input().split())

def solution(board, r, c):
    dd = [[-1,0],[1,0],[0,-1],[0,1]]

    for i in range(4):
        r1, c1 = r+dd[i][0], c+dd[i][1]
        if not(0<=r1<5 and 0<=c1<5) or board[r1][c1]==-1:
            continue
        
        b1 = [row[:] for row in board]

        get_apple1 = 1 if b1[r1][c1] == 1 else 0

        b1[r][c] = -1

        for j in range(4):
            r2, c2 = r1+dd[j][0], c1+dd[j][1]
            if not(0<=r2<5 and 0<=c2<5) or b1[r2][c2]==-1:
                continue
            
            b2 = [row[:] for row in b1]

            get_apple2 = get_apple1 + (1 if b2[r2][c2] == 1 else 0)

            b2[r1][c1] = -1

            if get_apple2 >= 2:
                return 1
            
            for k in range(4):
                r3, c3 = r2+dd[k][0], c2+dd[k][1]
                
                if not(0<=r3<5 and 0<=c3<5) or b2[r3][c3]==-1:
                    continue

                get_apple3 = get_apple2 + (1 if b2[r3][c3] == 1 else 0)

                if get_apple3 >= 2:
                    return 1
    return 0

print(solution(board, r, c))

# 2) 재귀로



# code ref: backjoon(26169) / joonlab(1116) / 알고리즘 분류: 완전탐색, 구현, 그래프이론, 깊이우선탐색, 백트래킹