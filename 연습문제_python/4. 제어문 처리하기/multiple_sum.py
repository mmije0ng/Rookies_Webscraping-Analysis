# range(시작, 끝+1, 간격)를 활용하여 3의 배수 리스트 생성
multiples = list(range(3, 101, 3))

# 리스트 내 요소들의 합계와 개수 계산
total_sum = sum(multiples)
count = len(multiples)

print(f"1부터 100까지 3의 배수: {multiples}")
print(f"3의 배수의 합: {total_sum}")
print(f"3의 배수의 개수: {count}개")