# 2751: 수 정렬하기 2 
import sys

n = int(sys.stdin.readline())
li = []

for _ in range(n):
    li.append(int(sys.stdin.readline()))

li.sort()

for i in li:
    print(i)


# code ref: backjoon(2751) / 알고리즘 분류: 정렬