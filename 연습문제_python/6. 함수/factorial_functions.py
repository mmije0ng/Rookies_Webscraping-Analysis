# 재귀 함수를 이용한 팩토리얼
def factorial_recursive(n):
    # 종료 조건: n이 1 이하일 때 1을 반환
    if n <= 1:
        return 1
    # n! = n * (n-1)! 원리를 이용
    return n * factorial_recursive(n - 1)

# 반복문을 이용한 팩토리얼
def factorial_iterative(n):
    result = 1
    # 1부터 n까지 차례대로 곱함
    for i in range(1, n + 1):
        result *= i
    return result

n1, n2 = 5, 7

print(f"{n1}! (재귀) = {factorial_recursive(n1)}")
print(f"{n1}! (반복) = {factorial_iterative(n1)}")
print(f"{n2}! (재귀) = {factorial_recursive(n2)}")
print(f"{n2}! (반복) = {factorial_iterative(n2)}")