dan = int(input("몇 단을 출력할까요? "))

print(f"{dan}단 구구단:")

# 1부터 9까지 반복 (range의 끝 값은 포함되지 않으므로 10으로 설정)
for i in range(1, 10):
    result = dan * i
    print(f"{dan} x {i} = {result}")