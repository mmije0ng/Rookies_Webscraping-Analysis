total_sum = 0
num = -1  # 0이 아닌 값으로 초기화하여 루프가 시작되도록 함

# num이 0이 아닌 동안 계속 반복
while num != 0:
    num = int(input("숫자를 입력하세요 (0을 입력하면 종료): "))
    total_sum += num

print(f"입력된 숫자들의 합: {total_sum}")