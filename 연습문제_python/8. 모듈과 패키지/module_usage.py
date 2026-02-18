import datetime
import random

# 1. datetime 모듈 활용
now = datetime.datetime.now()
print(f"현재 날짜와 시간: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# 한글 요일 출력을 위한 리스트 (0: 월요일 ~ 6: 일요일)
weekdays = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
weekday_name = weekdays[now.weekday()]

# 날짜 포맷팅 출력
formatted_date = now.strftime("%Y년 %m월 %d일")
print(f"포맷된 날짜: {formatted_date} {weekday_name}")

# 2. random 모듈 활용
# 1~10 사이의 임의의 정수 (1과 10 포함)
rand_int = random.randint(1, 10)
print(f"임의의 숫자: {rand_int}")

# 0~10 사이의 임의의 실수
rand_float = random.uniform(0, 10)
print(f"임의의 실수: {rand_float:.2f}")

# 리스트에서 임의의 요소 선택
fruits = ['사과', '바나나', '딸기', '포도', '오렌지']
rand_fruit = random.choice(fruits)
print(f"임의의 리스트 요소: {rand_fruit}")

# 리스트 요소 섞기 (원본 리스트 순서 변경)
random.shuffle(fruits)
print(f"섞인 리스트: {fruits}")