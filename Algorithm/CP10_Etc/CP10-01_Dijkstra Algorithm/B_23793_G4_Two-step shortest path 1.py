# 23793: 두 단계 최단 경로 1
 
# 시간초과 발생 코드
N, M = map(int, input().split())
E = list([] for _ in range(N+1))
for _ in range(M):
    u, v, w = map(int, input().split())
    E[u].append([v, w])
X, Y, Z = map(int, input().split())

from queue import PriorityQueue 
INF = int(1e18)

def dijkstra(num, edges, s, e, m=False):
    visited = [False] * (num+1)
    D = [INF] * (num+1)
    pq = PriorityQueue()

    if m:
        visited[m] = True

    D[s] = 0
    pq.put([0, s])

    while pq:
        cost, here = pq.get()

        if D[here] < cost or visited[here]:
            continue 

        visited[here] = True 

        if here == e:
            return D[here]
    
        for there, c in E[here]:
            next_cost = cost + c 
        
            if not visited[there] and next_cost < D[there]:
                D[there] = next_cost
                pq.put([next_cost, there])

    return -1 


xy = dijkstra(N, E, X, Y, False)
yz = dijkstra(N, E, Y, Z, False)
xyz = dijkstra(N, E, X, Z, Y)
if xy == -1 or yz == -1:
    print(-1, end=' ')
else:
    print(xy+yz, end = ' ')

print(xyz)

# 시간 초과 2
import heapq

INF = int(1e18)

def dijkstra(num, edges, s, e, block=False):
    visited = [False] * (num+1)
    D = [INF] * (num+1)
    pq = []

    if block:
        visited[block] = True

    D[s] = 0
    heapq.heappush(pq, (0, s))

    while pq:
        cost, here = heapq.heappop(pq)

        if D[here] < cost or visited[here]:
            continue 

        visited[here] = True 

        if here == e:
            return D[here]
    
        for there, c in edges[here]:
            next_cost = cost + c 
        
            if not visited[there] and next_cost < D[there]:
                D[there] = next_cost
                heapq.heappush(pq, (next_cost, there))

    return -1 


xy = dijkstra(N, E, X, Y)
yz = dijkstra(N, E, Y, Z)
xyz = dijkstra(N, E, X, Z, Y)
if xy == -1 or yz == -1:
    print(-1, end=' ')
else:
    print(xy+yz, end = ' ')

print(xyz)

# 에러 해결 코드
import sys
import heapq

input = sys.stdin.readline
INF = int(1e18)

N, M = map(int, input().split())
E = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    E[u].append((v, w))

X, Y, Z = map(int, input().split())

def dijkstra(num, edges, s, e, block=0):
    visited = [False] * (num+1)
    D = [INF] * (num+1)
    pq = []

    if block:
        visited[block] = True

    D[s] = 0
    heapq.heappush(pq, (0, s))

    while pq:
        cost, here = heapq.heappop(pq)

        if D[here] < cost or visited[here]:
            continue 

        visited[here] = True 

        if here == e:
            return cost 
    
        for there, c in edges[here]:
            next_cost = cost + c 
        
            if not visited[there] and next_cost < D[there]:
                D[there] = next_cost
                heapq.heappush(pq, (next_cost, there))

    return -1 


xy = dijkstra(N, E, X, Y)
yz = dijkstra(N, E, Y, Z)
xyz = dijkstra(N, E, X, Z, Y)

if xy == -1 or yz == -1:
    ans1 = -1
else:
    ans1 = xy + yz

sys.stdout.write(f"{ans1} {xyz}\n")

# code ref: backjoon(23793) / 알고리즘 분류: 그래프 이론, 최단 경로, 데이크스트라