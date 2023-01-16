# EXERCISE 07
# 비밀 언어 우비두비 단어 만들기

# # 복습 - 내 풀이
# def pl_sentence(sentence):
#     word_list = sentence.split()
#     for i in word_list:
#         if i[0] in 'aeiou':
#             print(f'{i}way', end = ' ')
#         else:
#             print(f'{i[1:]}{i[0]}ay', end = ' ')
    
# pl_sentence('this is a test translation')

# # 복습 - 해답지 풀이
# def pl_sentence(sentence):
#     output = []
#     for word in sentence.split():
#         if word[0] in 'aeiou':
#             output.append(f'{word}way')
#         else:
#             output.append(f'{word[1:]}{word[0]}ay')
#     return ' '.join(output)

# print(pl_sentence('this is a test'))

# # 풀이 도전
# def ubbi_dubbi(word):
#     word_list = list((word))
#     for i in word_list:
#         if i in 'aeiou':
#             print('ub{}'.format(i), end = '')
#     else:
#         print('{}'.format(i), end = '')

# print(ubbi_dubbi('elephant'))

# 
def ubbi_dubbi(word):
    output = []
    for letter in word:
        if letter in 'aeiou':
            output.append(f'ub{letter}')
        else:
            output.append(letter)
    return ''.join(output)

print(ubbi_dubbi('python'))



