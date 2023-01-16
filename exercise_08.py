# EXERCISE 08
# 문자열 정렬하기

# # 복습
# def ubbi_dubbi(word):
#     output =[]
#     for i in word:
#         if i in 'aeiou':
#             output.append(f'ub{i}')
#         else:
#             output.append(f'{i}')
#     print(''.join(output))


# ubbi_dubbi('octopus')
# ubbi_dubbi('elephant')


# # 풀이 도전
# def strsort(word):
#     word_list = sorted(word)
#     print(''.join(word_list))

def strsort(word):
    return ''.join(sorted(word))


print(strsort('cba'))
print(strsort('chicken'))
print(strsort('computer'))