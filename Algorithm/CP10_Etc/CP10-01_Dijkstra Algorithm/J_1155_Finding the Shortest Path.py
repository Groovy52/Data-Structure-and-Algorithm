# 1155: 최단 경로 구하기
N, M = map(int, input().split())
E = list([] for _ in range(N + 1))
for _ in range(M):
    u, v, w = map(int, input().split())
    E[u].append([v, w])
X, Z = map(int, input().split())

N, M, E, X, Z

from queue import PriorityQueue

INF = int(1e18)

def dijkstra(N, E, X, Z):
    visited = [False]* (N+1) # 방문 여부 처리
    D = [INF] *(N+1) # 모든 원소의 값을 무한대로 초기화하는 1차원 배열 D
    pq = PriorityQueue() # 거리가 확정된 정점을 저장하는 1차원 배열이자 우선 순위 큐

    D[X] = 0
    """
    S는 “최단 거리가 이미 확정된 정점들의 집합” 
    반면 우선순위 큐는 “아직 확정되지 않았지만, 현재까지 계산된 후보 거리들 중 가장 작은 것을 빨리 꺼내기 위한 자료구조
    """
    pq.put([0, X]) # 

    while pq: # while pq.empty()==False:
        cost, here = pq.get()

        # 지금 꺼낸 게 더 크면 무시 / 또는/ 방문했으면 무시
        if D[here] < cost or visited[here] == True:
            continue 

        visited[here] = True 

        if here ==Z: # 도착:
            return D[here]
        
        # 인접정점
        for there, c in E[here]:
            next_cost = cost + c 
        
            if not visited[there] and next_cost < D[there]: 
                D[there] = next_cost
                pq.put([next_cost, there])


    return -1


# code ref: joonlab(1155) / 알고리즘 분류: 최단 경로 