"""
Docstring for CP01-01_String > string_methods.py

# Method 

- strip() / strip(str): 문자열의 시작과 끝에 공백/문자 제거
- split(구분문자): 구분문자를 기준으로 문자열을 구분하여 리스트의 개별 요소로 반환
  - "111,222,333"을 쉼표 ,로 구분하고 싶을 때, "111,222,333".split(",")하면
  - ["111", "222", "333"]을 반환
- upper() / lower(): 문자열을 대문자로 / 소문자로 반환 
- "".join(리스트): split과 반대역할을 하는 method, ["111","222","333"]을 "111,222,333"으로 반환하려면
  - ",".join(["111","222","333"])으로 하면 됨.
- replace('old','new'): old 문자열을 new 문자열로 교체
- eval("문자열"): 문자열의 진위값 판별 => 출력값 : bool (True/ Flase)
- find("문자열"): 처음 발견된 문자열의 인덱스 반환

# Formating method

- % format
- str.format()
- f-string format

"""

# -----------------------------
#   strip 함수 예제
# -----------------------------

"""
strip 함수 설명:
- 문자열.strip(): 양쪽 공백 제거
- 문자열.strip(특정문자): 양쪽 특정문자 제거
- 문자열.lstrip(): 왼쪽 제거
- 문자열.rstrip(): 오른쪽 제거
- 입력값: 문자열, 출력값: 문자열
"""

# 공백 제거
data = '   안녕   '
text = data.strip()
text2 = data.lstrip()
text3 = data.rstrip()

print(text)   # '안녕'
print(text2)  # '안녕   '
print(text3)  # '   안녕'


# 특정 문자열 제거  
data = '###안녕###'
text = data.strip('#')
text2 = data.lstrip('#')
text3 = data.rstrip('#')

print(text)   # '안녕'
print(text2)  # '안녕###'
print(text3)  # '###안녕'


# -----------------------------
#   split 함수 예제
# -----------------------------

"""
split 함수 설명:
- 문자열.split(): 공백(스페이스, 탭, 줄바꿈)을 기준으로 문자열을 나눔
- 문자열.split(구분자): 지정한 문자(문자열)를 기준으로 나눔
- 입력값: 문자열 / 출력값: 리스트
"""

# 기본 공백 기준 분리
text = "Python is very powerful"
result1 = text.split()
print(result1) # ['Python', 'is', 'very', 'powerful']


# 특정 문자 기준 분리
data = "apple,banana,grape,orange"
result2 = data.split(",")
print(result2) # ['apple', 'banana', 'grape', 'orange']


# 여러 개의 공백이 있어도 자동 처리
text2 = "  Hello   World   Python  "
result3 = text2.split()
print(result3) # ['Hello', 'World', 'Python']


# -----------------------------
#   upper(), lower() 함수 예제
# -----------------------------

"""
문자열.upper(), .lower(), .swapcase():
- 변환함수: 소문자를 대문자로, vice versa, 양방향(소->대, 대->소)
- 입력값: 문자열 / 출력값: 문자열 

문자열.isupper(), .islower():
- 확인함수: 주어진 문자가 대문자인지 소문자인지 확인
- 위 함수 또는 if str == str.lower() 또는 if str == str.upper()를 사용할 수 있음
"""

str = 'ArithmeticError'

# 대소문자 서로 바꾸기 1
print(str.swapcase()) # 'aRITHMETICeRROR'

# 대소문자 서로 바꾸기 2
answer = ''
for s in str:
    if s.isupper():
        answer += s.lower()
    else:
        answer += s.upper()
        
print(answer) # 'aRITHMETICeRROR'


# -----------------------------
#   join 함수 예제
# -----------------------------

"""
join 함수 설명:
- '구분자'.join(리스트): 리스트의 각 요소를 구분자로 연결하여 하나의 문자열로 만듦
- 리스트나 튜플, 기타 이터러블(iterable)의 문자열 요소들을 하나로 합칠 때 사용
- 모든 요소는 문자열(str)이어야 함 (정수나 다른 타입이면 str()로 변환해야 함)
- 입력값: 리스트나 튜플, 기타 이터러블(iterable)의 문자열 / 출력값: 문자열
"""

# 리스트의 문자열 요소를 연결
words = ['Python', 'is', 'awesome']
sentence = ' '.join(words)
print(sentence) # Python is awesome


# 쉼표(,)로 연결
fruits = ['apple', 'banana', 'grape']
result = ', '.join(fruits) # apple, banana, grape
print(result)


# 줄바꿈 문자로 연결
lines = ['line1', 'line2', 'line3']
result = '\n'.join(lines)
print(result)
# 출력:
# line1
# line2
# line3


# 숫자 리스트를 join하려면 str로 변환 필요
nums = [1, 2, 3]
# map(str, nums)를 통해 문자열로 변환
result = '-'.join(map(str, nums))
print(result) # 1-2-3


# 한 줄 문자열을 문자 한개당 다음 줄로 넘겨 여러줄로 출력하는 작업
str = 'ArithmeticError'
print('\n'.join(str))

# 출력
# A
# r
# i
# t
# h
# m
# e
# t
# i
# c
# E
# r
# r
# o
# r


"""
특수문자 또는 '작은 따옴표 또는 "큰 따옴표를 문자열의 일부로 표현하고 싶을 때:
- 앞에 r, 양쪽에 '작은 따옴표로 감싸주면 됨
"""

# 주어진 문자열 = !@#$%^&*(\'"<>?:;
print(r'!@#$%^&*(\'"<>?:;')


# -----------------------------
#   replace 함수 예제
# -----------------------------

"""
replace 함수 설명:
- 문자열.replace(기존문자, 새로운문자): 문자열 내의 특정 부분을 다른 문자열로 바꾼다.
- 변경된 새로운 문자열을 반환하며, 원래 문자열은 변경되지 않는다 (문자열은 immutable)
- 존재하지 않는 문자열을 바꾸려고 하면 아무 일도 일어나지 않는다
- 선택적으로 바꿀 횟수(count)를 지정할 수도 있다: 문자열.replace(기존문자, 새로운문자, 횟수)
"""

# 기본 사용 예시
text = "I love apples. Apples are sweet."
result = text.replace("apples", "oranges")
print(result) # I love oranges. Apples are sweet. (소문자로 시작하는 apples 만 oranges로 변경)


# 대소문자 구분 주의
result2 = text.replace("Apples", "Bananas")
print(result2) # I love apples. Bananas are sweet.


# 횟수 제한 (count 매개변수)
text2 = "ha ha ha ha"
result3 = text2.replace("ha", "ho", 2) # 앞에서부터 n번만 바꿈
print(result3) # ho ho ha ha


# 존재하지 않는 문자
result4 = text.replace("grapes", "peaches")
print(result4) # I love apples. Apples are sweet. (변경될 문자가 없음->변화X)


# -----------------------------
#   eval 함수 예제
# -----------------------------

"""
eval 함수 설명:
- eval(expression)
- 입력값: 문자열 / 출력값: bool (True or False)
"""

str ='5 >= 10' 
print(eval(str)) # False


# -----------------------------
#   find 함수 예제
# -----------------------------

"""
find 함수 설명:
- find(문자열)
- 입력값: 문자열 / 출력값: int (처음 발견된 문자열의 인덱스를 반환)
"""
s = "Python is Scripting Language"
str ='is'

print(s.find(str)) # 7


# -----------------------------
#   % format 예제
# -----------------------------
name = 'Daeseok'
print("Hello %s" % name) # "Hello Deaseok"

name = "daeseok"
age = 30
print("my name is %s, age is %d." % (name, age)) # "my name is daeseok, age is 30."

# -----------------------------
#   % str.format 예제
# -----------------------------
print("Hello, my name is {} and I'm {}".format(name, age)) # "Hello, my name is daeseok and I'm 30"

print("Hello, my name is {1} and I'm {0}".format(age, name)) # "Hello, my name is daeseok and I'm 30"

whoami = {'name': 'daeseok', 'age': 30}
print("Hello, my name is {name} and I'm {age}".format(name = whoami['name'], age = whoami['age'])) # "Hello, my name is daeseok and I'm 30"

print("Hello, my name is {name} and I'm {age}".format(**whoami)) # "Hello, my name is daeseok and I'm 30"


# -----------------------------
#   % f-string 예제
# -----------------------------
print(f"Hello, my name is {name} and I'm {age}")
