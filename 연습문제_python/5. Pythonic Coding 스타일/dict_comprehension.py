# 1부터 5까지의 숫자를 키로, 그 제곱을 값으로 하는 딕셔너리 생성
squares_dict = {i: i ** 2 for i in range(1, 6)}

# 1부터 10까지 중 짝수만 골라 제곱 딕셔너리 생성 (if 조건문 활용)
even_squares_dict = {i: i ** 2 for i in range(1, 11) if i % 2 == 0}

print(f"1부터 5까지의 제곱 딕셔너리: {squares_dict}")
print(f"짝수만의 제곱 딕셔너리: {even_squares_dict}")