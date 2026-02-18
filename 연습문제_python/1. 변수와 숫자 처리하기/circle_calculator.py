# 1. 사용자로부터 반지름 입력 받기 (소수점 입력도 가능하도록 float 사용)
radius = float(input("원의 반지름을 입력하세요: "))

# 2. 원주율 정의
PI = 3.14159

# 3. 계산 수행
area = PI * (radius ** 2)    # 반지름의 제곱은 ** 2 를 사용합니다.
circumference = 2 * PI * radius

# 4. 결과 출력 (소수점 둘째 자리까지 반올림)
print(f"반지름이 {radius}인 원의 넓이: {area:.2f}")
print(f"반지름이 {radius}인 원의 둘레: {circumference:.2f}")