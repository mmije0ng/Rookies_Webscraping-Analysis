# 학생 이름과 점수를 매핑한 딕셔너리 생성
grades = {
    "김철수": 85,
    "이영희": 92,
    "박민수": 78,
    "최수진": 95
}

print("학생 성적:")
# items() 메서드를 사용하여 이름과 점수를 동시에 반복 추출
for name, score in grades.items():
    print(f"{name}: {score}점")

# values() 메서드를 사용하여 점수 데이터만 추출 후 평균 계산
all_scores = grades.values()
average = sum(all_scores) / len(all_scores)

print(f"평균 점수: {average}점")