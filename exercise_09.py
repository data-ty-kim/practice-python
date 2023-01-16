# EXERCISE 09
# 처음과 마지막 요소 찾기

# # 복습
# def strsort(word):
#     return (''.join(sorted(word)))

# print(strsort('chicken'))

# # 풀이 도전
# def firstlast(seq):
#     seq[0]
#     seq[-1]

def firstlast(seq):
    return seq[:1] + seq[-1:]


print(firstlast('abcd'))
print(firstlast((1,2,3,4)))
print(firstlast([1,2,3,4]))
