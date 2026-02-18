import os
import sys

# 1. 현재 작업 디렉토리 및 시스템 정보
print(f"현재 작업 디렉토리: {os.getcwd()}")
print(f"Python 버전: {sys.version}")
print(f"운영체제: {os.name}")

# 2. 환경 변수 PATH 출력 (가독성을 위해 일부만 출력)
path_env = os.environ.get('PATH', '')
print(f"환경 변수 PATH 일부: {path_env[:50]}...")

# 3. 파일 경로 다루기
full_path = "/Users/username/documents/report.txt"

# 경로에서 디렉토리와 파일명 분리
directory = os.path.dirname(full_path)
filename = os.path.basename(full_path)

# 파일명과 확장자 분리
name_only, extension = os.path.splitext(filename)

print("\n파일 경로 정보:")
print(f"- 디렉토리: {directory}")
print(f"- 파일명: {filename}")
print(f"- 확장자: {extension}")

# 4. 파일 존재 여부 확인
exists = os.path.exists(full_path)
print(f"파일 존재 여부: {exists}")