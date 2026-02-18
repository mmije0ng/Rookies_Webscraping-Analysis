# 인사말과 추가 메시지에 기본값을 설정한 함수
def greeting(name, message="안녕하세요", extra=""):
    # 추가 메시지가 있을 경우와 없을 경우를 처리
    full_message = f"{message}, {name}님!"
    if extra:
        full_message += f" {extra}"
    
    # 영어권 이름을 위해 '님'이 어색한 경우를 고려한 단순 출력 로직
    if message == "Hello":
        return f"{message}, {name}!"
        
    return full_message

# 1. 기본값 '안녕하세요' 사용
print(greeting("김철수"))

# 2. 인사말 변경 ('Hello')
print(greeting("John", message="Hello"))

# 3. 모든 매개변수 활용 (추가 메시지 포함)
print(greeting("이영희", extra="좋은 하루 되세요!"))