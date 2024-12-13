string = input()

alphabet_occurrence_array = [-1] * 26

for i, char in enumerate(string):
    index = ord(char) - ord('a')
    if alphabet_occurrence_array[index] == -1:  # 첫 등장일 때만 기록
        alphabet_occurrence_array[index] = i

# 결과를 공백으로 구분하여 출력
print(" ".join(map(str, alphabet_occurrence_array)))