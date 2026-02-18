email = input("이메일 주소를 입력하세요: ")

# '@' 기호를 기준으로 문자열 분리 (리스트 형태로 반환됨)
# split('@')은 @를 기준으로 왼쪽과 오른쪽을 나누어 리스트에 담음
parts = email.split('@')

# 리스트의 첫 번째 요소는 사용자명, 두 번째 요소는 도메인
username = parts[0]
domain = parts[1]

print(f"사용자명: {username}")
print(f"도메인: {domain}")