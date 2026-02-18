# 사용자 정의 모듈 임포트
import math_operations as mo

# 원의 넓이 (반지름 5)
circle = mo.get_circle_area(5)
# 직사각형 넓이 (가로 10, 세로 5)
rect = mo.get_rectangle_area(10, 5)
# 팩토리얼 5!
fact = mo.get_factorial(5)
# 최대공약수 (48, 18)
gcd_val = mo.get_gcd(48, 18)

print(f"원의 넓이: {circle:.2f}")
print(f"직사각형 넓이: {rect}")
print(f"팩토리얼 5! = {fact}")
print(f"최대공약수(48, 18) = {gcd_val}")