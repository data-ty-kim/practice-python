# EXERCISE 06
# 피그 라틴 문장 만들기

# # 복습
# def pig_latin(word):
#     if word[0] in 'aeiou':
#         print(f'{word}way')
#     else:
#         print(f'{word[1:]}{word[0]}ay')


# pig_latin('air')
# pig_latin('eat')
# pig_latin('python')
# pig_latin('computer')

# 풀이 도전
def pl_sentence(sentence):
    word_list = sentence.split()
    for i in word_list:
        if i[0] in 'aeiou':
            print(f'{i}way', end = ' ')
        else:
            print(f'{i[1:]}{i[0]}ay', end = ' ')


pl_sentence('this is a test translation')

