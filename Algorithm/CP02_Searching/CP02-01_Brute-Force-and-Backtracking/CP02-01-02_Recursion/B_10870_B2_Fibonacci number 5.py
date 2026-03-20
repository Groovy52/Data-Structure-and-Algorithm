# 10870: 피보나치 수 5

n = int(input())

def f(n):
    
    if n==0:
        return 0
    elif n <=2:
        return 1 
    else:
        return f(n-1) + f(n-2)

print(f(n))

# code ref: backjoon(10870) / 알고리즘 분류: 수학, 구현

