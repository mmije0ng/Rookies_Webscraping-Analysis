import datetime

name = "김철수"
age = 25
pi = 3.14159
price = 1234
percentage = 0.855
today = datetime.date(2025, 7, 20)

# f-string을 이용한 다양한 포매팅
print(f"이름: {name}, 나이: {age}")

# 소수점 둘째 자리까지 출력
print(f"원주율: {pi:.2f}")

# 천 단위 콤마 추가
print(f"가격: {price:,}원")

# 퍼센트 형식 (소수점 둘째 자리까지)
print(f"퍼센트: {percentage:.2%}")

# 날짜 형식 지정
print(f"날짜: {today:%Y년 %m월 %d일}")