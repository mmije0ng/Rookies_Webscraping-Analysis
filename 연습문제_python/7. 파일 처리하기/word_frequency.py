from collections import Counter
import os

# 분석할 샘플 텍스트 파일 생성 (동일)
sample_text = "파이썬 프로그래밍 언어 배우기 쉬운 언어 파이썬 강력한 파이썬 프로그래밍"
with open("data/text_sample.txt", "w", encoding="utf-8") as f:
    f.write(sample_text)

# 1. 파일 읽기 및 단어 리스트 생성
with open("data/text_sample.txt", "r", encoding="utf-8") as f:
    words = f.read().split()

# 2. Counter를 사용하여 한 줄로 빈도 계산
word_counts = Counter(words)

# 3. most_common() 메서드로 빈도순 정렬된 결과 가져오기
print("단어 빈도 분석 결과:")
for word, count in word_counts.most_common():
    print(f"{word}: {count}번")