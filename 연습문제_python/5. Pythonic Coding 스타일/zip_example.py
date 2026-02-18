students = ['김철수', '이영희', '박민수', '최수진']
scores = [85, 92, 78, 95]

# zip을 사용하여 학생명과 점수를 동시에 순회
print("학생과 점수 매칭:")
for name, score in zip(students, scores):
    print(f"{name}: {score}점")

# zip으로 묶인 객체를 dict() 함수에 넣어 바로 딕셔너리로 변환
student_dict = dict(zip(students, scores))

print(f"점수별 학생 딕셔너리: {student_dict}")