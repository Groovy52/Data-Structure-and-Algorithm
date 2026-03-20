# 너비 우선 탐색(Breadth-First Search)과 깊이 우선 탐색(Depth-First Search)

# 1) 알고리즘의 동작 과정을 보여주기 위해 먼저 탐색할 자료구조인 이진 트리를 정의한다. 
    # 노드 기본 선언 코드
class Node:
    def __init__(self, data):
        self.left = None 
        self.right = None 
        self.data = data 

    def __repr__(self):
        return str(self.data)
    
    # 이진 트리 작성 코드        
class BinarySearchTree:
    def __init__(self):
        self.__root = None 
    
    def insert(self, data):
        self.__root = self._insert_rec(self.__root, data)
    
    def _insert_rec(self, node, data):
        if not node:
            node = Node(data)

        else:
            if node.data > data:
                node.left = self._insert_rec(node.left, data)
            else:
                node.right = self._insert_rec(node.right, data)

        return node 

    # 2) bfs, dfs를 위해 밖에서 root를 전달할 함수
    def get_root(self):
        return self.__root


# 3) 트리 선언
#              20
#            /    \
#          14      25
#         /  \    /  \
#       11   18  23   30
#           /    /
#         15    21

bst = BinarySearchTree()
bst.insert(20)
bst.insert(25)
bst.insert(14)
bst.insert(30)
bst.insert(23)
bst.insert(18)
bst.insert(11)
bst.insert(21)
bst.insert(15)

# 너비 우선 탐색(BFS)
"""
- 너비 우선 탐색은 트리(그래프) 시작 정점(노드)에서 인접한 정점을 먼저 탐색하는 방법이다.
- 너비 우선 탐색이라는 이름에서 알 수 있듯이 너비를 우선하는 것이니 그래프 또는 트리의 같은 레벨에 있는 모든 노드를 1번으로 접근한다고 보면 된다. 
- 특징:
    - 너비 우선 탐색에서 중요한 키워드는 "큐(Queue)"이다.
    - 큐 자료구조를 사용하면 먼저 입력으로 들어간 데이터가 먼저 꺼내어지는 FIFO (First In First Out) 특징을 가진다.
- 활용:
    - 너비 우선 탐색 알고리즘으로 트리의 노드를 방문하거나 노드의 데이터를 처리할 수 있다.
    - 또는 그래프의 정점을 방문하여 정답을 구하는 문제도 너비 우선 탐색 알고리즘을 이용하여 해결할 수 있다.
"""
# 너비 우선 탐색의 알고리즘을 구현하기 위해 deque함수를 이용해 나중에 queue를 선언한다
from collections import deque

def bfs(root):
    if root is None:
        print('tree is empty')
        return 
    
    # queue 를 선언한다.
    queue = deque()
    result = [] 

    queue.append(root)

    while queue:
        node = queue.popleft()
        result.append(node.data)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        

    print(f'bread first search: {result}')

# 너비 우선 탐색 동작 확인
bfs(bst.get_root()) # bread first search: [20, 14, 25, 11, 18, 23, 30, 15, 21]

# 깊이 우선 탐색(DFS)
"""
- 깊이 우선 탐색은 트리(그래프) 시작 정점(노드)의 자식 정점을 하나 방문한 다음 아래로 내려갈 수 있을 때까지 내려가면서 정점을 방문하는 방법이다.
- 더 내려가서 방문할 정점이 없으면 위로 되돌아오면서 내려갈 수 있는 정점이 있으면 바로 내려간다.
- 특징:
    - 깊이 우선 탐색에서 중요한 키워드는 "스택(Stack)"이다.
    - 스택 자료구조를 사용하면 나중에 입력으로 들어간 데이터가 먼저 꺼내어지는 LIFO (Last In First Out) 특징을 가진다.
    - 재귀적 접근, 반복적 접근의 두가지 작성 방식이 있다.
- 활용:
    - 깊이 우선 탐색 알고리즘으로 트리의 노드를 방문하거나 노드의 데이터를 처리할 수 있다.
    - 또는 그래프의 정점을 방문하여 정답을 구하는 문제도 깊이 우선 탐색 알고리즘을 이용하여 해결할 수 있다.
"""
# 1) 반복 접근
def dfs_iter(root):
    if root is None:
        print('tree is empty')
        return 
    
    # stack을 선언한다.
    stack = []
    result = [] 

    stack.append(root)

    while stack:
        node = stack.pop()
        result.append(node.data)

        if node.right: # 왼쪽, 오른쪽의 순서는 중요하진 않지만 이진 탐색 트리, 보편적인 방문순서를 기준으로 왼쪽부터 추가하기 위해 오른쪽을 먼저 방문해준다 (스택의 LIFO)
            stack.append(node.right)

        if node.left:
            stack.append(node.left)
        
    print(f'depth first search: {result}')


dfs_iter(bst.get_root()) # depth first search: [20, 14, 11, 18, 15, 25, 23, 21, 30]

# 2) 재귀 접근
def dfs_rec(node, result):
    if node is None:
        print('tree is empty')
        return 
    
    result.append(node.data)
    if node.left:
        dfs_rec(node.left, result)
    if node.right:
        dfs_rec(node.right, result)
        
"""
result(res_rec)를 전역 변수로 선언하지 않아도 함수 내에서 변경된 값을 밖에서 출력했을 때 변화된 값이 출력되고, 에러 발생하지 않음
=> global이 필요 없는 이유는 전역 변수 res_rec 자체를 다시 대입한 게 아니라, 그 리스트 객체 내부를 수정했기 때문
=> 만약 함수 내에서 res_rec += 1을 실행했다면, res_rec = res_rec + 1과 같아
"""
res_rec = [] # stack 선언

dfs_rec(bst.get_root(), res_rec)
print(f'depth first search: {res_rec}') # depth first search: [20, 14, 11, 18, 15, 25, 23, 21, 30]


# ref: 책. 쓰면서 익히는 알고리즘과 자료구조 / 6장. 트리(Tree) / 6.3 깊이 우선 탐색(Depth-First Search) & 6.4 너비 우선 탐색(Breadth-First Search)