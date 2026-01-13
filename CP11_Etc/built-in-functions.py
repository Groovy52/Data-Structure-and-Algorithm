"""
Docstring for CP11_Etc > built-in-functions.py

"""

# -----------------------------
#   map 함수 예제
# -----------------------------

"""
map 함수 설명:
- map(function, iterable): iterable의 각 요소에 function을 적용
- 결과는 map 객체로 반환되므로, list()로 감싸서 결과 확인
- 첫 번째 매개변수로는 함수(int가 올 수도 있음-숫자로 반환)가 오고 두 번째 매개변수로는 반복 가능한 자료형     (리스트, 튜플 등)이 올 수 있음.
- for 반복문 같은 걸 이용해서 하나하나 리스트 요소에 접근할 필요가 없음 (원소별 적용될 함수와 원소가 포함된 리스트 또는 튜플만 넣어주면 됨)
"""

# Ex 1. function
a, b = map(int, ['5', '3'])
print(a, type(a)) # 5 <class 'int'>
print(b, type(b)) # 3 <class 'int'>


# Ex 2. 리스트에 있는 값에 1씩 더해서 새로운 리스트를 반환하는 작업
oriList = [1, 2, 3, 4, 5]

## 방법 1. map 함수 이용
def add_one(n):
    return n + 1

newList = list(map(add_one, oriList))
print(newList) # [2, 3, 4, 5, 6]

## 방법 2. for 반복문 이용
newList = []
for val in oriList:
    newList.append(val+1)
    
print(newList) # [2, 3, 4, 5, 6]


# -----------------------------
#   not 함수 예제
# -----------------------------

"""
not 함수 설명: 
- 비어있거나 0인 입력값이 bool로 표현했을 때 False라면 not함수는 그 bool 을 뒤집어서 True를 반환.
- 입력값: 모든 자료형 / 출력값: bool 자료형 (입력이 True면 False & vice versa)
"""

# 0 제외 모든 수 = False
print(not(0), not(1)) # (True, False)

print('') # True

print(not([])) # True


# -----------------------------
#   int 함수 예제
# -----------------------------

"""
int 함수 설명:
- bool 자료형을 숫자로 반환
- 입력: bool (True or False) / 출력: int (1 or 0)
- True면 1, False면 0
"""

# int(bool)
print(int(True)) # 1

# int(if result -> bool)
number = 100
n = 3
m = 2
print(int(number % n == 0 & number % m == 0)) # 0


# -----------------------------
#   sum 함수 예제
# -----------------------------

# start, end, step => sum
print(sum(range(1,10,2))) # 25

answer = 0
for i in range(1,10,2):
    print(f'sum this value: {i}')
    answer += i
print(f'final answer: {answer}')
# 출력:
# sum this value: 1
# sum this value: 3
# sum this value: 5
# sum this value: 7
# sum this value: 9
# final answer: 25


# sum(list)
print(sum([1,-1])) # 0


# -----------------------------
#   zip 함수 예제
# -----------------------------

"""
zip 함수 설명:
- zip(iterable1, iterable2, ...): 여러 iterable(리스트, 튜플 등)의 요소들을 **병렬로 묶어주는 함수**
- 각 iterable에서 같은 인덱스끼리 튜플로 묶어줌
- 결과는 zip 객체로 반환되며, list()로 감싸서 출력할 수 있음
- 길이가 다른 경우, **가장 짧은 iterable 기준**으로 묶임
"""

# 두 리스트 병렬 묶기
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]

zipped = list(zip(names, scores))
print(zipped) # [('Alice', 85), ('Bob', 92), ('Charlie', 78)]


# 세 개 이상도 가능
ages = [25, 30, 22]
zipped3 = list(zip(names, scores, ages))
print(zipped3) # [('Alice', 85, 25), ('Bob', 92, 30), ('Charlie', 78, 22)]


# 길이가 다른 경우
short_list = [1, 2]
long_list = ['a', 'b', 'c']
result = list(zip(short_list, long_list))
print(result) # [(1, 'a'), (2, 'b')]  -> 짧은 쪽 기준으로 자름


# unzip (역으로 풀기): zip(*) 사용
zipped = [('A', 1), ('B', 2), ('C', 3)]
letters, numbers = zip(*zipped)
print(letters)  # ('A', 'B', 'C')
print(numbers)  # (1, 2, 3)

# dictionary에서 각각을 key와 value로 묶음
dict(zip(['w','s','d','a'], [1,-1,10,-10])) # {'w': 1, 's': -1, 'd': 10, 'a': -10}