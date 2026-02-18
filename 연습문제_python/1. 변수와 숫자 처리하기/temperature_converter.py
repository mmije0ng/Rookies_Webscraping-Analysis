# 1. 사용자로부터 섭씨 온도(Celsius)를 입력받음
# 온도에는 소수점이 포함될 수 있으므로 float 형으로 변환
celsius = float(input("섭씨 온도를 입력하세요: "))

# 2. 화씨 온도(Fahrenheit) 변환 공식을 적용
# 화씨 = 섭씨 * 9/5 + 32
fahrenheit = (celsius * 9 / 5) + 32

# 3. 결과 출력
# 결과값이 정수처럼 보이더라도 77.0과 같이 실수 형태로 출력되도록 구성
print(f"섭씨 {celsius:g}도는 화씨 {fahrenheit:.1f}도입니다.")