# EXERCISE 12
# 특정 글자를 가장 많이 가진 단어 찾기

#복습
PEOPLE = [{
    'first' : 'Reuven', 'last' : 'Lerner',
    'email' : 'reuven@lerner.co.il'
}, {
    'first' : 'Donald', 'last' : 'Trump',
    'email' : 'president@whitehouse.gov'
}, {
    'first' : 'Vladimir', 'last' : 'Putin',
    'email' : 'president@kremvax.ru'

}]

# from operator import itemgetter

# def alphabetize_names(dict):
#     return sorted(dict, key = itemgetter('last', 'first'))

# print(alphabetize_names(PEOPLE))

# def alphabetize_names(dict):
#     for person in sorted(dict, key = lambda x: [x['last'], x['first']])

# 풀이도전
words = ['this', 'is', 'an', 'elementary', 'test', 'example']
from collections import Counter
# print(dir(Counter))
# help(Counter.most_common)

def A(string):
    return Counter(string).most_common(1)[0][1]

def B(list):
    return max(list, key = A)

print(B(words))

    
    
