# 10989: 수 정렬하기 3

# 메모리 초과 1)
N = int(input())
num_list = [int(input()) for _ in range(N)]

num_list.sort()
for n in num_list:
    print(n)

# 메모리 초과 2)
import sys
input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
count = [0] * 10001

for _ in range(N):
    count[int(input())] += 1

for i in range(1, 10001):
    if count[i] > 0:
        write((str(i) + '\n') * count[i])

# 시간 초과
N = int(input())
count = [0]*10001 # 10,000

for _ in range(N):
    count[int(input())] += 1

for i in range(1, 10001):
    for _ in range(count[i]):
        print(i)

# 에러 발생 x 코드
import sys
input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
count = [0] * 10001

for _ in range(N):
    count[int(input())] += 1

for i in range(1, 10001):
    for _ in range(count[i]):
        write(str(i) + '\n')


# code ref: backjoon(10989) / 알고리즘 분류: 정렬