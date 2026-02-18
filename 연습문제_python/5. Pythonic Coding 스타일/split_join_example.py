text = "Python is awesome programming language"

# 문자열을 공백 기준 리스트로 분리
words = text.split()

# 리스트 요소를 하이픈(-)으로 연결
hyphen_text = "-".join(words)

# 각 단어를 대문자로 변환한 리스트를 만든 후 공백으로 연결
# 리스트 컴프리헨션을 사용하여 가독성 높임
upper_text = " ".join([w.upper() for w in words])

print(f"원본 문자열: {text}")
print(f"분리된 단어들: {words}")
print(f"하이픈으로 연결: {hyphen_text}")
print(f"대문자로 변환 후 공백으로 연결: {upper_text}")