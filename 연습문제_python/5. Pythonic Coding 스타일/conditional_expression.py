# 1. 기본적인 삼항 연산자 (True일 때 값 if 조건 else False일 때 값)
score = 85
result = "합격" if score >= 80 else "불합격"

# 2. 다른 예시: 성인 판별
age = 17
status = "성인" if age >= 19 else "미성년자"

# 3. 함수 인자 내에서 직접 사용
num1, num2 = 42, 15
max_val = num1 if num1 > num2 else num2

# 4. 리스트 컴프리헨션과 결합 (조건에 맞는 데이터만 필터링)
numbers = [5, -3, 12, 0, 8, -1, 23]
positives = [n for n in numbers if n > 0]

print(f"점수: {score}, 결과: {result}")
print(f"나이: {age}, 상태: {status}")
print(f"숫자들의 최대값: {max_val}")
print(f"양수들: {positives}")