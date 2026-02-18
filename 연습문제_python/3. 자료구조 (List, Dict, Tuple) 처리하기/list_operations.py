list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# 리스트를 세트로 변환하여 집합 연산 수행
set1 = set(list1)
set2 = set(list2)

# 합집합 연산(|)으로 병합 및 중복 제거 후 리스트로 변환
combined_list = sorted(list(set1 | set2))

# 교집합 연산(&)으로 공통 요소 추출 후 리스트로 변환
common_elements = sorted(list(set1 & set2))

print(f"리스트1: {list1}")
print(f"리스트2: {list2}")
print(f"병합된 리스트: {combined_list}")
print(f"공통 요소: {common_elements}")