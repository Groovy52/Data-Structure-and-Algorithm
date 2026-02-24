# 24416: 알고리즘 수업 - 피보나치 수 1

n = int(input())

# 피보나치 값을 DP로 계산 (재귀로 하면 시간 낭비)
f = [0] * (n + 1)
f[1] = f[2] = 1

for i in range(3, n + 1):
    f[i] = f[i - 1] + f[i - 2]

code1 = f[n]      # 코드1 실행 횟수 = F(n)
code2 = n - 2     # 코드2 실행 횟수 = 반복문 횟수 (n + 1) - 3 = n - 2

print(code1, code2)

# 아래는 잘못된 코드 -> 문제 의사코드를 그대로 작성할 필요 없음, 재귀로 풀면 시간초과 발생
n = int(input())

global fib_count 
fib_count = 0

def fib(n):
    global fib_count
    if n==1 or n==2:
        fib_count += 1
        return 1
    else:
        return (fib(n-1) + fib(n-2))

global fibonacci_count 
fibonacci_count = 0

def fibonacci(n):
    global fibonacci_count 
    f = [0]*(n+1)
    f[1] = f[2] = 1
    for i in range(3, n+1):
        fibonacci_count += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]

fib(n)
fibonacci(n)

print(fib_count, fibonacci_count)

# code ref: backjoon(24416) / 알고리즘 분류: 수학, 동적 계획법 