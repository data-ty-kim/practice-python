# EXERCISE 35A
# 게마트리아 (1)

# 복습
def get_sv(filename):
    word_sets = set()
    vowel_set = set('aeiou')
    with open(filename, 'r', encoding =' UTF8') as f:
        for word in f:
            if vowel_set < set(word.strip()):
                word_sets.add(word.strip())
    return word_sets

# print(get_sv('C:/Users/user/Documents/words.txt'))

# 복습해답
def get_sv_0(filename):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return {word.strip()
        for word in open(filename)
        if vowels < set(word.lower())
    }


# # 풀이 도전
# gemma_dict = {key : value 
#                 for key in 'abcdefghijklmnopqrstuvwxyz'
#                 for value in range(1,27)}
# print(gemma_dict)

# 해답
import string

def gematria_dict():
    return {char : index
            for index, char
            in enumerate(string.ascii_lowercase, 1)}

# print(gematria_dict())


# exercise 35B
# 게마트리아 (2)

# # 복습
# gematria_dict_review = {key : value 
#                     for value, key in enumerate('abcdefghijklmnopqrstuvwxyz', 1)}
# # print(gematria_dict_review)

# # 풀이도전
# def gematria_for(word):
#     return sum((gematria_dict_review[i] for i in word))

# # print(gematria_for('cat'))

# def gematria_equal_words(word):
#     gema_value = gematria_for(word)
#     gema_list = []
#     with open('C:/Users/user/Documents/words.txt', 'r', encoding = 'UTF8') as f:
#         for j in f:
#             if gematria_for(j.strip().lower()) == gema_value:
#                 gema_list.append(j)
#     return gema_list

# gematria_equal_words('cat')


# 해답
GEMATRIA = gematria_dict()

def gematria_for(word):
    return sum(GEMATRIA.get(one_char, 0) for one_char in word)

def gematria_equal_words(input_word):
    our_score = gematria_for(input_word.lower())
    return [one_word.strip() 
            for one_word in open('C:/Users/user/Documents/words.txt')
            if gematria_for(one_word.lower()) == our_score]

print(gematria_equal_words('cat'))