numbers1 = [2, 4, 6, 8, 10]
numbers2 = [1, 3, 5, 7, 12]

# numbers1 검사
# 리스트 컴프리헨션(또는 제너레이터 표현식)과 조합하여 사용
all_even1 = all(num % 2 == 0 for num in numbers1)
any_over_10_1 = any(num > 10 for num in numbers1)

print(f"숫자 리스트: {numbers1}")
print(f"모든 수가 짝수인가? {all_even1}")
print(f"하나라도 10보다 큰 수가 있는가? {any_over_10_1}\n")

# numbers2 검사
all_even2 = all(num % 2 == 0 for num in numbers2)
any_over_10_2 = any(num > 10 for num in numbers2)

print(f"숫자 리스트2: {numbers2}")
print(f"모든 수가 짝수인가? {all_even2}")
print(f"하나라도 10보다 큰 수가 있는가? {any_over_10_2}")