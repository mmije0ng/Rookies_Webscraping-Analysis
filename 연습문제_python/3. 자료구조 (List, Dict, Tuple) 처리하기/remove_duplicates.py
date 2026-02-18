original_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# set 자료형으로 변환하여 중복 요소 자동 제거
unique_set = set(original_list)

# 다시 리스트로 변환 후 오름차순 정렬
sorted_list = sorted(list(unique_set))

print(f"원본 리스트: {original_list}")
print(f"중복 제거 후: {sorted_list}")