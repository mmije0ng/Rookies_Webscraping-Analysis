# 더하기 함수
def add(a, b):
    return a + b

# 빼기 함수
def subtract(a, b):
    return a - b

# 곱하기 함수
def multiply(a, b):
    return a * b

# 나누기 함수
def divide(a, b):
    # 0으로 나누는 경우를 대비한 간단한 처리
    if b == 0:
        return "0으로 나눌 수 없습니다."
    return a / b

x, y = 10, 5

print(f"{x} + {y} = {add(x, y)}")
print(f"{x} - {y} = {subtract(x, y)}")
print(f"{x} * {y} = {multiply(x, y)}")
print(f"{x} / {y} = {divide(x, y)}")