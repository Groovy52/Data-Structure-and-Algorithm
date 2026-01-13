"""
Docstring for CP02_Linear-Structure.CP02-01_List.CP02-01-01_Array.basic

# List 
- **연속된 메모리 공간**에 데이터를 저장하는 자료구조

## (1) Linear List = Array (Python)
- 인덱스를 통한 **빠른 접근(O(1))**
- 중간 원소 삽입/삭제 시 **원소개수만큼 (O(n))** 데이터 이동 비용 발생

## (2) Linked List
- 노드(Node)가 **포인터로 연결된 구조**
- 메모리가 연속적이지 않아도 됨
- 삽입/삭제가 효율적, 접근은 느림

"""

# Linear List (Array)

## 리스트 초기화
py_list_empty = []
print(py_list_empty) # []

## 0을 10개 가지는 리스트 초기화 (1)
py_list_zeros_1 = [0 for i in range(10)]
print(py_list_zeros_1) # [0,0,0,0,0,0,0,0,0,0]

## 0을 10개 가지는 리스트 초기화 (2)
py_list_zeros_2 = [0] * 10
print(py_list_zeros_2) # [0,0,0,0,0,0,0,0,0,0]

# ----------------------------------------------------- #

## 리스트 요소 추가 및 삭제
py_list = [1,2,3,4,5]
py_list.append(6)
print(py_list)  # [1,2,3,4,5,6]

# 요소 추가 => (1) append (2) extend (3) insert
## (1) append(요소)
py_list_1 = [1,2,3]
py_list_2 = [4,5,6]
py_list_1.append(py_list_2)
print(py_list_1) # [1,2,3,[4,5,6]]

## (2) extend(요소) 
py_list_1 = [1,2,3]
py_list_2 = [4,5,6]
py_list_1.extend(py_list_2)
print(py_list_1) # [1,2,3,4,5,6]

## (3) insert(추가될 위치 인덱스(0부터 시작), 요소)
py_list_1 = [1,2,3]
py_list_1.insert(3, 4) # 3번째 위치에 4 요소 추가
print(py_list_1) # [1,2,3,4]

# ----------------------------------------------------- #

# 요소 삭제 => (1) remove (2) clear (3) del
## (1) .remove(요소) => 삭제하려는 요소가 2개 이상이라면, 가장 앞선 인덱스의 요소를 삭제한다
py_list_1 = [1,2,3,2,4]
py_list_1.remove(2) # 2 요소 삭제 
print(py_list_1) # [1,3,2,4]

## (2) .clear() => 모든 요소를 삭제 
py_list_1 = [1,2,3]
py_list_1.clear()
print(py_list_1) # []

## (3) del list[위치 인덱스]
py_list = [1,2,3]
del py_list[1] # 1번째 인덱스에 있는 삭제
print(py_list) # [1,3]
