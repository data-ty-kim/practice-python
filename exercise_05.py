# EXERCISE 05
# 피그 라틴 단어 만들기

# # 복습
# def name_tri():
#     name = input('What is your name?: ')
#     for index, letter in enumerate(name):
#         print(name[0:index+1])

# name_tri()

# 풀이 도전
# def pig_latin():
#     pig_word = input('Enter your word: ')
#     if pig_word[0] in ['a', 'e', 'i', 'o', 'u']:
#         pig_word_0 = pig_word + 'way'
#     else:
#         pig_word_0 = pig_word[1:] + pig_word[0] + 'ay'
    
#     print(pig_word_0)

# pig_latin()
# # 1트만에 성공!

def pig_latin(word):
    if word[0] in 'aeiou':
        return f'{word}way'
    return f'{word[1:]}{word[0]}ay'

print(pig_latin('eat'))
print(pig_latin('air'))
print(pig_latin('python'))
print(pig_latin('computer'))