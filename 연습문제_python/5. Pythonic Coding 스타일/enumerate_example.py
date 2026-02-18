fruits = ['사과', '바나나', '오렌지', '포도', '딸기']

# enumerate를 사용하여 인덱스(index)와 값(fruit)을 동시에 추출
print("과일 목록:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")