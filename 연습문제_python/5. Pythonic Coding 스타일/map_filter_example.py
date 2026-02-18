numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map을 사용하여 모든 수의 제곱 계산
squared_numbers = list(map(lambda x: x ** 2, numbers))

# filter를 사용하여 5보다 큰 수만 추출
filtered_numbers = list(filter(lambda x: x > 5, numbers))

# filter와 map을 조합하여 5보다 큰 수들의 제곱 계산
# 5보다 큰 수를 먼저 거르고(filter), 그 결과에 제곱을 적용(map)
filtered_squared = list(map(lambda x: x ** 2, filter(lambda x: x > 5, numbers)))

print(f"원본 숫자: {numbers}")
print(f"모든 수의 제곱: {squared_numbers}")
print(f"5보다 큰 수들: {filtered_numbers}")
print(f"5보다 큰 수들의 제곱: {filtered_squared}")