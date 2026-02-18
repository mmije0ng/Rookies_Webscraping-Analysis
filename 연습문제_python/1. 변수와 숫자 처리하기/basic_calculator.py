# input()은 기본적으로 문자열(string)로 저장되므로 정수형(int)으로 변환해줌
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))

# 사칙연산 수행 및 결과 출력
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")

# 나눗셈의 경우 소수점 둘째 자리까지 표시하기 위해 round 함수를 사용하거나 
# f-string의 포맷팅 기능을 활용 가능
print(f"{num1} / {num2} = {num1 / num2:.2f}")