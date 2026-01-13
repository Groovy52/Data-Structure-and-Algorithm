"""
# 연결 리스트 (Linked List)의 이해

- 각 자료가 다음 자료에 연결 고리를 가진 자료구조 
- 데이터를 가진 하나의 요소 = node
- 각 node에는 데이터 값과 주소값을 가진다(다음 노드를 연결하기 위한)

# 배열 VS 연결 리스트
- 배열은 고정 크기를 가지지만, 연결 리스트는 데이터를 동적 크기를 가진다.
- 삽입 시,
    - 배열은 해당 위치값을 넣고 그 인덱스에 위치하는 값을 뒤로 옮겨주는 작업이 필요하지만
    - 연결 리스트는 데이터의 연결 고리만 변경해주면 된다.
- 접근 시, 
    - 배열은 인덱스를 이용해 특정 위치의 데이터에 접근할 수 있지만
    - 연결 리스트는 처음부터 순회해야 한다.
    
"""

# 연결 리스트 연산(Linked List calculation)
from typing import Any 

class Node:
    def __init__(self, data: Any):
        self.data = data 
        self.next = None 

node = Node(3)
print(f'{node.data}') # 3


node1 = Node(11)
node2 = Node(12)
node3 = Node(13)

node1.next = node2
node2.next = node3


# 연결 리스트 순회(Linked List traverse)
from typing import Any 

class Node:
    def __init__(self, data: Any):
        self.data = data 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 
        
    def traverse(self):
        temp = self.head 
        
        while temp:
            print(temp.data, end = " ")
            temp = temp.next
        print()
        
linked_list = LinkedList()

node1 = Node(11)
linked_list.head = node1 

node2 = Node(12)
node3 = Node(13)

node1.next = node2
node2.next = node3

print(linked_list.traverse()) # 11 12 13
