# EXERCISE 34
# 모든 모음을 포함하는 단어 찾기

# #복습
# d = {'a' : 1, 'b' : 2, 'c' : 3}
# func_sq = (lambda x : x**2)

# def transform_values(func, input_dict):
#     return {key : func(value) for key, value in input_dict.items()}

# print(transform_values(func_sq, d))

# # 도전
# def get_sv(filename):
#     vowel_set = set()
#     with open(filename, 'r', encoding = 'UTF8') as f:
#         for word in f:
#             for i in range(len(word)):
#                 if not word[i] in 'aeiou':
#                     pass
#                 else:
#                     vowel_set.add(word)
        
# 정답
def get_sv(filename):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return {word.strip() 
            for word in open(filename) 
            if vowels < set(word.lower())}

# print(len(get_sv('C:/Users/user/Documents/words.txt'))    )