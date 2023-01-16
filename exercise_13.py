# EXERCISE 13
# 튜플 레코드 출력하기

# # 복습
# words = ['this', 'is', 'an', 'elementary', 'test', 'example']

# from collections import Counter

# def func_a(string):
#     return Counter(string).most_common(1)[0][1]

# def most_repeating_word(list):
#     return max(list, key = func_a)

# print(most_repeating_word(words))

PEOPLE = [('Donald', 'Trump', 7.85),
        ('Vladimir', 'Putin', 3.626),
        ('Jinping', 'Xi', 10.603)]


# # 풀이 도전
# def format_sort_records(list):
#     for i in list:
#         for firstname, lastname, time in i:
#             return '{0:10} {1:10} {2:5.2d}'.format('lastname', 'firstname', 'time')

# print(format_sort_records(PEOPLE))

import operator
def format_sort_records(list):
    output = []
    template = '{1:10} {0:10} {2:5.2f}'
    for person in sorted(list, key = operator.itemgetter(1,0)):
        output.append(template.format(*person))
    
    return output

print('\n'.join(format_sort_records(PEOPLE)))