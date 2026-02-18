text = input("문자열을 입력하세요: ")
target_char = input("찾을 문자를 입력하세요: ")

# 문자열 내에 특정 문자가 포함된 횟수 계산
count_result = text.count(target_char)

print(f"문자 '{target_char}'이 {count_result}번 나타납니다.")