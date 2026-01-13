# Python VS C/C++
"""

| Type code | C 언어 타입        | Python 타입 | 최소 크기 (byte) |
|-----------|--------------------|-------------|------------------|
| `b`       | signed char        | int         | 1                |
| `c`       | char               | str (1자)   | 1                |
| `h`       | short              | int         | 2                |
| `i`       | int                | int         | 4                |
| `l`       | long               | int         | 4                |
| `q`       | long long          | int         | 8                |
| `f`       | float              | float       | 4                |
| `d`       | double             | float       | 8                |

"""


# Python의 Array 모듈
"""
- C에서 사용하는 배열 접근을 단순히 Wrapper하여 지원하는 Array 모듈
- Python 의 Array 모듈은 C/C++에서 사용하는 배열 접근을 그대로 제공하기 위한 모듈이다.
- 리스트는 여러 타입의 요소를 가질 수 있으나, 
- Array 모듈은 한 번 설정한 타입의 요소만 추가 / 삭제 가능하다.
"""

# ---------------------------------------------------------- #
import array as arr 

int_arr  =arr.array('i', [1,2,3])

## 1. Array 모듈을 통한 삽입/삭제
import array as arr 

int_arr = arr.array('i', [1,2,3])

### 요소 print
print("elements in array : ", end = "")
for i in range(len(int_arr)):
    print(int_arr[i], end = " ") 
    
print() # elements in array : 1 2 3

### 요소 삽입 => (인덱스, 요소)
print("elements after insertion : ", end = "")
int_arr.insert(1, 4)
for i in (int_arr):
    print(i, end = " ")

print() # elements after insertion : 1 4 2 3

### 요소 삭제 => 1 값을 찾아 제거 
int_arr.remove(1)
# 앞에 \ 역 슬래시를 붙이면 문자로 인식
print("elements after delete \'1\' in array : ", end = "")
for i in (int_arr):
    print(i, end = " ")
print() # elements after delete '1' in array : 4 2 3


# ---------------------------------------------------------- #
## 2. Array 모듈을 통한 배열 접근 및 값 업데이트
import array as arr 

# list 선언
int_list = [1,2,3,4,3,6,7,4,5,10] 

# list 요소를 배열로 변환
int_arr = arr.array('i', int_list)

# 3의 값이 가장 처음 나타나는 배열의 인덱스를 출력
print(int_arr.index(3)) # 2

# 1의 값이 가장 처음 나타나는 배열의 인덱스를 출력
print(int_arr.index(1)) # 0

# 배열 4번째 요소의 값을 5로 업데이트
int_arr[4] = 5
for i in (int_arr):
    print(i, end = " ")
print()  # 1 2 3 4 5 6 7 4 5 10

## code ref: 쓰면서 익히는 알고리즘과 자료구조/Array