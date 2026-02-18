import os

# 1. 'data' 폴더 확인 및 로그 파일 경로 설정
directory = "data"
if not os.path.exists(directory):
    os.makedirs(directory)

log_file = os.path.join(directory, "system.log")

# 2. 샘플 로그 데이터 생성
log_content = """2025-07-20 09:15:00 - WARNING - 메모리 사용량이 높습니다
2025-07-20 10:00:00 - INFO - 시스템 정상 가동 중
2025-07-20 10:30:00 - ERROR - 데이터베이스 연결 실패
2025-07-20 11:45:00 - ERROR - 파일을 찾을 수 없음
2025-07-20 12:00:00 - WARNING - 디스크 공간 부족"""

with open(log_file, "w", encoding="utf-8") as f:
    f.write(log_content)

print("로그 파일이 생성되었습니다.\n")

# 3. 로그 필터링 함수 정의
def filter_logs(file_path, level):
    print(f"{level} 레벨 로그들:")
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            # 해당 라인에 특정 레벨 문자열이 포함되어 있는지 확인
            if f"- {level} -" in line:
                print(line.strip())
    print() # 가독성을 위한 빈 줄

# 4. 결과 출력
filter_logs(log_file, "ERROR")
filter_logs(log_file, "WARNING")