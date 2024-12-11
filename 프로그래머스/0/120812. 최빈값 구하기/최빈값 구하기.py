from collections import Counter

# 길이 1~99, 0~999
def solution(array):
    counter = Counter(array)
    most_common = counter.most_common()
    max_count = most_common[0][1]  # 가장 높은 빈도
    duplicates = [num for num, count in most_common if count == max_count]

    if len(duplicates) > 1:
        return -1
    else:
        return duplicates[0]


solution([1, 2, 3, 3, 3, 4])  # 결과는 최빈값 3
solution([1, 1, 2, 2])        # 결과는 -1
solution([1])                 # 결과는 1