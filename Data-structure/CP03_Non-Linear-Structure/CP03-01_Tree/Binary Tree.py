"""
클래스(class)
- 데이터의 기능을 묶어 새로운 객체 타입을 만드는 문법
- 클래스 내부에 정의된 함수 = 메소드(method)

인스턴스(instance)
- 클래스로부터 만들어진 실제 객체(object)

__init__
- 파이썬에서 클래스의 생성자(constructor) 메소드
- 클래스의 인스턴스를 생성할 때 자동으로 호출되며, 인스턴스가 생성될 때 초기화 작업을 수행하는 메소드

self
- 파이썬에서 클래스의 인스턴스(instance)를 나타내는 변수로 클래스를 정의할 때 메소드의 첫 번째 매개변수로 반드시 사용되어야 하는 특별한 변수
"""

class Node:
    def __init__(self, data): # data = 생성 시 전달받을 값
        # 아래 세 줄 = 인스턴스의 속성을 붙여서 상태를 저장
        self.left = None
        self.right = None
        self.data = data
    
    def __repr__(self): # repr = representation, 출력 시 읽기 좋게 하기 위함 => 보통 __repr__ 또는 __str__로 표현
        return str(self.data)

root = Node(11) # 클래스 객체를 호출하면 그 클래스의 인스턴스 생성
print(root)