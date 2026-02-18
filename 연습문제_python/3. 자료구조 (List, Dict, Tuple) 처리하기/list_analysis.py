numbers = [15, 3, 27, 8, 19, 12, 31]

# 내장 함수를 사용하여 최댓값과 최솟값 산출
max_val = max(numbers)
min_val = min(numbers)

# 리스트를 오름차순으로 정렬
numbers.sort()

# 뒤에서 두 번째 인덱스(-2)를 사용하여 두 번째로 큰 값 추출
second_max = numbers[-2]

print(f"숫자 목록: [15, 3, 27, 8, 19, 12, 31]")
print(f"최댓값: {max_val}")
print(f"최솟값: {min_val}")
print(f"두 번째로 큰 값: {second_max}")