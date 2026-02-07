class Node:

    def __init__(self, data):
        self.left = None
        self.right = None 
        self.data = data 
    
    def __repr__(self):
        return str(self.data)    
    
# =========================== 이진탐색트리 (삽입연산) ===========================
   
class BinarySearchTree:
    def __init__(self):
        self.__root = None # 시작 상태 = 트리 비어있음
    
    # 삽입 => 1) 재귀 2) 반복법
    def insert(self, data, method='iterative'):
        if method == 'recursion': 
            self.__root = self._insert_rec(self.__root, data) # 재귀
        else:
            self._insert_iter(data) # 반복 
    
    # 재귀    
    def _insert_rec(self, node, data):
        if not node:
            node = Node(data)
        else:
            if node.data > data:
                # node의 left 가 차 있는 상태일 수 있으므로 
                # 기존 node.left와 현재 data를 비교하는 과정 필요
                node.left = self._insert_rec(node.left, data)
            else:
                # left와 마찬가지로 기존 node.right와 현재 data를 비교하는 과정 필요
                node.right = self._insert_rec(node.right, data)
            
        return node 
    
    # 반복
    def _insert_iter(self, data):
        # root is None
        if not self.__root:
            self.__root = Node(data)
            return 
        # create new node
        new_node = Node(data) # 아직 어느 위치에 붙일지 모르니까 연결은 나중에 함.
        
        curr = self.__root # 지금 보고 있는 노드 (처음엔 루트)
        parent = None # curr의 직전 노드(부모). 아직 루트의 부모는 없으니 None
        
        while (curr != None): # curr이 존재하는 동안 루프 반복
            parent = curr
            if curr.data > data:
                curr = curr.left
            else:
                curr = curr.right 
                
        if parent.data > data:
            parent.left = new_node
        else:
            parent.right = new_node
    
    # =========================== 순회 (중위 순회) ===========================
    def inorder_traverse(self):
        result = []
        self._inorder_rec(self.__root, result)
        return result 
    
    def _inorder_rec(self, node, result):
        if not node:
            return 
        
        self._inorder_rec(node.left, result)
        result.append(node.data)
        self._inorder_rec(node.right, result)
    
    def inorder_iter(self):
        result = []
        stack = []
        
        node = self.__root 
        
        while node or stack:
            while node:
                stack.append(node)
                node = node.left 
            if stack:
                node = stack.pop() # 마지막에 삽입된 것 부터 = 가장 말단의 왼쪽 자식 노드부터, 꺼내줌!
                result.append(node) # 위에서 꺼낸 순서대로 result에 추가
                node = node.right 
        return result
  
    # =========================== 탐색 (find) ===========================
    def find(self, data):
        return self._find_data(self.__root, data)
    
    def _find_data(self, node, data):
        if node is None: # 비교하려는 노드의 값이 비어있으면 False 반환
            return False
        elif node.data == data: # 값을 찾으면 True 반환
            return True
        elif node.data > data: # 찾으려는 값이 비교하는 값보다 작으면
            return self._find_data(node.left, data)
        else:
            return self._find_data(node.right, data)
    
    # =========================== 삭제 (delete) ===========================
    # delete (3가지 경우 )=============== ????
    def find_min_node(self, node):
        while node.left:
            node = node.left 
        return node 

    def delete(self, data):
        self._delete_data(self.__root, data)
    
    def _delete_data(self, node, data):
        parent = None
        curr = node
        
        # data에 해당하는 노드 찾기, parent 추적
        while curr and curr.data != data:
            parent = curr 
            
            if curr.data > data:
                curr = curr.left 
            else:
                curr = curr.right
            # data를 못찾는 경우
            if curr is None:
                return node 
            
            # 1. 삭제하려는 노드가 자식이 없는 leaf node인 경우
            if curr.left is None and curr.right is None:
                if curr != node:
                    if parent.left == curr:
                        parent.left = None
                    else:
                        parent.right = None 
                else:
                    node = None 
                
            # 2. 자식노드가 왼쪽, 오른쪽 모두 있는 경우
            elif curr.left and curr.right:
                # 지우려는 노드의 오른쪽 하위 트리에서 가장 작은 노드 찾기
                min_node = self.find_min_node(curr.right)
                min_data = min_node.data 
                
                # 오른쪽 하위 트리에서 가장 작은 노드는
                # 항상 leaf 노드이므로 그냥 삭제 진행
                self._delete_data(node, min_data)
                curr.data = min_data 
                
            # 3. 오른쪽 또는 왼쪽 노드 한개의 자식 노드만 있는 경우
            else:
                if curr.left:
                    child = curr.left 
                else:
                    child = curr.right 
                
                if curr != node:
                    if curr == parent.left:
                        parent.left = child 
                    else:
                        parent.right = child 
                else:
                    node = child 
            
            return node
            
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

print(bst.inorder_traverse())

print(f'find 25: {bst.find(25)}')
print(f'find 0: {bst.find(0)}')