import math

def get_circle_area(radius):
    """원의 넓이를 계산합니다."""
    return math.pi * (radius ** 2)

def get_rectangle_area(width, height):
    """직사각형의 넓이를 계산합니다."""
    return width * height

def get_factorial(n):
    """팩토리얼을 계산합니다."""
    if n <= 1:
        return 1
    return n * get_factorial(n - 1)

def get_gcd(a, b):
    """최대공약수를 계산합니다."""
    return math.gcd(a, b)