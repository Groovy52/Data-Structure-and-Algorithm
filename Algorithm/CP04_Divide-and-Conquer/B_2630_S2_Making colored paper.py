# 2630: 색종이 만들기

import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

def divide(x, y, size):
    global white, blue

    # 현재 검사할 영역의 첫 번째 칸의 색을 기준값으로 저장
    first = paper[x][y]

    # 현재 영역이 모두 같은 색인지 표시하는 변수
    same = True

    # 현재 영역(size x size)을 모두 확인 
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != first:
                same = False
                break
        if not same:
            break

    # 모두 같은 색이면 색종이 개수 증가
    if same:
        # 흰색이면 흰색 색종이 개수 증가
        if first == 0:
            white += 1
        # 파란색이면 파란색 색종이 개수 증가
        else:
            blue += 1
        # 더 이상 자를 필요 없으므로 함수 종료
        return

    # ---------------------------
    # 분할 (Divide)
    # 현재 영역이 한 가지 색이 아니므로 4등분
    # ---------------------------
    half = size // 2

    # ---------------------------
    # 정복 (Conquer)
    # 나눈 4개의 영역을 각각 재귀적으로 해결
    # ---------------------------
    divide(x, y, half)                 # 1사분면 (왼쪽 위)
    divide(x, y + half, half)          # 2사분면 (오른쪽 위)
    divide(x + half, y, half)          # 3사분면 (왼쪽 아래)
    divide(x + half, y + half, half)   # 4사분면 (오른쪽 아래)

divide(0, 0, n)

print(white)
print(blue)

# 더 간단하게 구현 =>
import sys
input = sys.stdin.readline

def divide(x, y, size):
    first = paper[x][y]

    # 더 이상 자를 수 없음 = 정사각형의 크기가 1이면 return
    if size == 1:
        result[first] += 1
        return

    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != first:
                size //= 2
                divide(x, y, size)                 
                divide(x, y + size, size)          
                divide(x + size, y, size)         
                divide(x + size, y + size, size) 
                return
            
    result[first] += 1

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
result = {0:0, 1:0}
divide(0, 0, n)

for i in result.values():
    print(i)


# code ref: backjoon(2630) / 알고리즘 분류: 분할 정복, 재귀