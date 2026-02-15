n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n-1):
    p, c = map(int, input().split())
    tree[p].append(c)
    
cost = [[] for _ in range(n)]
for i in range(n):
    w, b = map(int, input().split())
    cost[i].append((w, b))
    
    
total_cost = 0
def minimum_cost(u, tree, cost, color=0):
    global total_cost 
    
    if u==None:
        return 
    
    total_cost += cost[u][0][color]
    for child in tree[u]:
        minimum_cost(child, tree, cost, int(not bool(color)))

result = []
def solution(tree, cost):
    global total_cost 
    
    for i in range(2):
        total_cost = 0
        minimum_cost(0, tree, cost, i) 
        result.append(total_cost)
    
    return result
    
print(min(solution(tree, cost)))

# 이 코드의 버그 찾기 0124
# code reference: joonlab(1509) / backjoon(25512) / 알고리즘 분류: 그래프이론, 그래프탐색, 이분그래프