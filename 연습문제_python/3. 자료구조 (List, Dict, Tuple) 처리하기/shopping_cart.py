# 상품명을 키로, 수량과 단가를 담은 리스트를 값으로 하는 딕셔너리 생성
cart = {
    "사과": {"quantity": 2, "price": 1000},
    "바나나": {"quantity": 3, "price": 800},
    "오렌지": {"quantity": 1, "price": 1500}
}

total_price = 0

print("쇼핑 카트:")
# 딕셔너리를 순회하며 개별 품목의 합계와 전체 총액 계산
for item, info in cart.items():
    qty = info["quantity"]
    unit_price = info["price"]
    subtotal = qty * unit_price
    
    print(f"{item}: {qty}개 (개당 {unit_price}원) = {subtotal}원")
    
    # 각 품목의 소계를 총 가격에 누적
    total_price += subtotal

print(f"총 가격: {total_price}원")