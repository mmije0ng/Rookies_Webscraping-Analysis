# 좌표를 튜플 형태로 저장
point1 = (0, 0)
point2 = (3, 4)

# 인덱싱을 사용하여 각 좌표 값 추출
# (x2 - x1)**2 + (y2 - y1)**2 계산
x_diff_sq = (point2[0] - point1[0]) ** 2
y_diff_sq = (point2[1] - point1[1]) ** 2

# 제곱근 계산을 위해 0.5 제곱 수행
distance = (x_diff_sq + y_diff_sq) ** 0.5

print(f"점1: {point1}")
print(f"점2: {point2}")
print(f"두 점 사이의 거리: {distance}")