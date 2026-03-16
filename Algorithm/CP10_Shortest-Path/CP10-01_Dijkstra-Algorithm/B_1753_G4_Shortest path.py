# 1753: 최단 경로

# 시간 초과 발생 
import sys 
sys.stdin.readline # 이 부분을 input = sys.stdin.readline으로 고쳐야 '시간 초과'가 발생하지 않음!!

V, E = map(int, input().split())
K = int(input())
edges = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))

import heapq
INF = int(1e18)

def dijkstra(V, K, graph):

    D = [INF]*(V + 1)
    selected = [False]*(V + 1)
    pq = []

    D[K] = 0
    heapq.heappush(pq, (0, K))

    while pq:
        cur_dist, now = heapq.heappop(pq)

        if selected[now]:
            continue 

        selected[now] = True
        
        for nxt_node, d in graph[now]:
            if not selected[nxt_node]:
                nxt_dist = cur_dist + d 

                if nxt_dist < D[nxt_node]: 
                    D[nxt_node] = nxt_dist 
                    heapq.heappush(pq, (nxt_dist, nxt_node))

    return D

dist = dijkstra(V, K, edges)

for i in range(V):
    if dist[i+1] == INF:
        sys.stdout.write('INF\n')
    else:
        sys.stdout.write(f'{dist[i+1]}\n')



# code ref: backjoon(1753) / 알고리즘 분류: 그래프 이론, 최단 경로, 데이크스트라