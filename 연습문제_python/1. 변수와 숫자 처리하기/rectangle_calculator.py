# 사용자로부터 가로와 세로 길이를 입력받음 (정수형 변환)
width = int(input("가로 길이를 입력하세요: "))
height = int(input("세로 길이를 입력하세요: "))

# 넓이와 둘레 계산
area = width * height
perimeter = (width + height) * 2

print(f"직사각형의 넓이: {area}")
print(f"직사각형의 둘레: {perimeter}")