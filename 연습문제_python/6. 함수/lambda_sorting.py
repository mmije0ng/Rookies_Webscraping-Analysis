# (이름, 점수) 형태의 튜플 리스트
students = [('김철수', 85), ('이영희', 92), ('박민수', 78), ('최수진', 95)]

# 1. 이름순 정렬 (튜플의 첫 번째 요소인 x[0] 기준)
name_sorted = sorted(students, key=lambda x: x[0])

# 2. 점수순 정렬 (튜플의 두 번째 요소인 x[1] 기준)
score_sorted = sorted(students, key=lambda x: x[1])

# 3. 점수 내림차순 정렬 (reverse=True 옵션 사용)
score_desc = sorted(students, key=lambda x: x[1], reverse=True)

print(f"학생 정보: {students}")
print(f"이름순 정렬: {name_sorted}")
print(f"점수순 정렬: {score_sorted}")
print(f"점수 내림차순: {score_desc}")