original_price = int(input("상품 가격을 입력하세요: "))
discount_rate = int(input("할인율을 입력하세요(%): "))

# 할인 금액과 최종 가격 계산
# 할인율을 100으로 나누어 비율(0.2 등)로 변환 후 계산
discount_amount = int(original_price * (discount_rate / 100))
final_price = original_price - discount_amount

print(f"원래 가격: {original_price}원")
print(f"할인율: {discount_rate}%")
print(f"할인 금액: {discount_amount}원")
print(f"최종 가격: {final_price}원")