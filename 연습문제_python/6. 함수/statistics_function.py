def get_statistics(numbers):
    count = len(numbers)
    avg = sum(numbers) / count
    maximum = max(numbers)
    minimum = min(numbers)
    
    # 표준편차 계산: 각 요소와 평균의 차이의 제곱의 합을 구함
    variance = sum((x - avg) ** 2 for x in numbers) / count
    std_dev = variance ** 0.5
    
    # 여러 값을 튜플 형태로 한꺼번에 반환
    return avg, maximum, minimum, std_dev

data = [10, 20, 30, 40, 50]

# 함수 호출 및 결과 언패킹
mean, high, low, sd = get_statistics(data)

print(f"숫자들: {data}")
print(f"평균: {mean:.1f}")
print(f"최댓값: {high}")
print(f"최솟값: {low}")
print(f"표준편차: {sd:.2f}")