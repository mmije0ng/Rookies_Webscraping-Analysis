# 튜플/리스트 언패킹
point = (10, 20)
x, y = point  # 좌항과 우항의 개수가 같으면 변수에 각각 대입됨

nums = [1, 2, 3]
a, b, c = nums

# 가변 위치 인수 (*args) 사용 예제
def sum_all(*args):
    # args는 함수 내부에서 튜플로 취급됨
    return sum(args)

# 가변 키워드 인수 (**kwargs) 사용 예제
def print_info(**kwargs):
    # kwargs는 함수 내부에서 딕셔너리로 취급됨
    info_str = ", ".join([f"{k}={v}" for k, v in kwargs.items()])
    print(f"키워드 인수들: {info_str}")

print(f"좌표: x={x}, y={y}")
print(f"리스트 언패킹: a={a}, b={b}, c={c}")
print(f"가변 인수의 합: {sum_all(10, 20, 30)}")
print_info(name="김철수", age=25, city="서울")