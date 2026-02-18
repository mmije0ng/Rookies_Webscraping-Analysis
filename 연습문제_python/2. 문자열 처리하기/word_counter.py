# 문자열 앞뒤의 화이트스페이스 제거
sentence = input("문장을 입력하세요: ").strip()

# 공백을 기준으로 단어들을 분리하여 리스트로 만듦
# split()에 인자를 주지 않으면 연속된 공백도 하나로 처리함
words = sentence.split()

# 분리된 단어들을 다시 하나의 공백으로 연결
cleaned_sentence = " ".join(words)

# 리스트의 요소 개수를 측정
word_count = len(words)

print(f"공백 제거: {cleaned_sentence}")
print(f"단어 개수: {word_count}개")