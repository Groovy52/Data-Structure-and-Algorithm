# 1927: 최소 힙
import sys
import heapq 
input = sys.stdin.readline 

n = int(input())
q = [] 
for _ in range(n):
    x = int(input())
    if x==0:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q, x)


# code ref: backjoon(1927) / 알고리즘 분류: 자료구조, 우선순위 큐 