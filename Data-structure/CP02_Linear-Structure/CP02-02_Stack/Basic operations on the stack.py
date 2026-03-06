"""

# 스택의 기본 연산들
- push / pop

## 연산 지원 방법
- list와 deque은 표면적으로는 동일한 사용 방법에 의해 동일한 결과를 가져올 수 있는데 내부적으로는 구현이 다르다.

### 1) list(리스트) 사용
- list는 연속적인 메모리 블록을 할당하여 공간을 하나씩 채워가는 형태
- deque와는 달리 만들어진 공간이 차면 추가적으로 확장해주는 작업이 필요하다.

### 2) deque(덱) 사용
- deque는 연결 리스트 구조여서 앞에서부터 접근하기 때문에 리스트의 인덱싱보다 조금 느리다.
- 데이터가 얼마큼 들어오는지 미리 정해 놓지 않아도 메모리가 허용하는 한 계속 추가할 수 있다.

"""

### 1) list
stack= []
stack.append(1)
stack.append(3)
stack.append(5)

stack.pop()
# 5
stack.pop()
# 3
stack.pop()
# 1
stack
# []

### 2) deque
from collections import deque 

stack = deque()

stack.append(3)
stack.append(1)
stack.append(5)

stack
# deque([3, 1, 5])

stack.pop()
# 5
stack.pop()
# 1
stack.pop()
# 3
stack
# []


# code ref: 쓰면서 익히는 알고리즘과 자료구조 / 4장 스택(Stack)과 재귀(Recursion)