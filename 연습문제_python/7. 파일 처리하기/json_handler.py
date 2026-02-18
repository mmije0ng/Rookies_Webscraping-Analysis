import json
import os

# 1. 저장할 폴더 생성
directory = "data"
if not os.path.exists(directory):
    os.makedirs(directory)

file_path = os.path.join(directory, "data.json")

# 2. 저장할 데이터 준비 (파이썬 딕셔너리 구조)
user_data = {
    "이름": "김철수",
    "나이": 25,
    "직업": "개발자",
    "취미": ["독서", "영화감상", "코딩"],
    "주소": "서울시 강남구"
}

# 3. JSON 파일로 저장하기
with open(file_path, "w", encoding="utf-8") as f:
    # indent=4는 들여쓰기를 적용해 사람이 보기 편하게 저장함
    # ensure_ascii=False는 한글이 깨지지 않고 그대로 저장되게 함
    json.dump(user_data, f, indent=4, ensure_ascii=False)

print(f"데이터가 {file_path}에 저장되었습니다.\n")

# 4. JSON 파일 읽어오기
print("JSON에서 읽어온 데이터:")
with open(file_path, "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    
    # 읽어온 데이터 출력
    for key, value in loaded_data.items():
        print(f"{key}: {value}")