import os

# 1. 저장할 디렉토리 설정 및 생성
directory = "data"
if not os.path.exists(directory):
    os.makedirs(directory)

file_path = os.path.join(directory, "test.txt")

# 2. 파일에 내용 쓰기 ('w' 모드)
lines = [
    "안녕하세요\n",
    "파이썬 파일 처리를 연습하고 있습니다\n",
    "오늘은 좋은 날씨입니다\n"
]

print("파일에 저장할 내용:")
for line in lines:
    print(line.strip())

# with 문을 사용하여 data/test.txt에 저장
with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("\n" + "-"*30 + "\n")

# 3. 파일에서 내용 읽어오기 ('r' 모드)
print(f"[{file_path}]에서 읽어온 내용:")
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()
    print(content)