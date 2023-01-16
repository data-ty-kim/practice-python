# EXERCISE 21
# 파일에서 가장 긴 단어 찾기

# # 복습
# def wc(file):
#     dict = {'글자 수' : 0, '단어 수' : 0, '줄 수' : 0, '유일한 단어 수' : 0}
#     unique_word = set()
#     with open(file, 'r', encoding = 'UTF8') as f:
#         for line in f:
#             dict['글자 수'] += len(line)
#             dict['단어 수'] += len(line.split())
#             dict['줄 수'] += 1
#             unique_word.update(line.split())  
#         dict['유일한 단어 수'] = len(unique_word)  
#     for key, value in dict.items():
#         print(f'{key:<12}:{value:>5}')

# wc('C:/Users/user/Documents/New_PC.txt')

import os

def find_longest_word(filename):
    longest_word = ''
    for one_line in open(filename, encoding = 'UTF8'):
        for one_word in one_line.split():
            if len(one_word) > len(longest_word):
                longest_word = one_word
    return longest_word

def find_all_longest_words(dirname):
    return {
        filename:
            find_longest_word(os.path.join(dirname, filename))
            for filename in os.listdir(dirname)
            if os.path.isfile(os.path.join(dirname, filename))
    }

print(find_all_longest_words('C:/Users/user/Downloads/books'))