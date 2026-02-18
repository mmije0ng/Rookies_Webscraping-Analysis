words = ['cat', 'elephant', 'dog', 'butterfly', 'ant']

# len(문자열 길이)을 기준으로 최댓값과 최솟값 검색
longest_word = max(words, key=len)
shortest_word = min(words, key=len)

# 결과 출력
print(f"단어 목록: {words}")
print(f"가장 긴 단어: {longest_word} ({len(longest_word)}글자)")
print(f"가장 짧은 단어: {shortest_word} ({len(shortest_word)}글자)")