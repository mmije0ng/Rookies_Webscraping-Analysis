import os

# 1. 'data' 폴더가 없으면 생성
if not os.path.exists("data"):
    os.makedirs("data")
    print("'data' 폴더가 생성되었습니다.")

# CSV 데이터 준비
raw_data = "김철수,85\n이영희,92\n박민수,78\n최수진,95"

# 파일 저장 (상대 경로 'data/' 사용)
file_path = "data/grades.csv"
with open(file_path, "w", encoding="utf-8") as f:
    f.write(raw_data)

print(f"학생 성적이 {file_path}에 저장되었습니다.\n")

# 2. 파일 읽기 및 성적 분석
scores = []
print("성적 분석 결과:")

with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        # 줄바꿈 제거 및 분리
        name, score_str = line.strip().split(",")
        score = int(score_str)
        scores.append(score)
        print(f"{name}: {score}점")

# 전체 평균 계산
average = sum(scores) / len(scores)
print(f"전체 평균: {average:.1f}점")