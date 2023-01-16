# EXERCISE 32
# 딕셔너리 반전하기

# # 복습
# def plword(word):
#     if word[0] in 'aeiou':
#         return word + 'way'
#     else:
#         return word[1:] + word[0] + 'ay'

# # print(plword('computer'))
# def plfile(filename):
#     return ' '.join(plword(word) 
#         for sentence in open(filename) 
#         for word in sentence.split())

d = {'a' : 1, 'b' : 2, 'c' : 3}

# 내 시도
def reverse_dict(sampledict):
    new_dict = {}
    for key, value in sampledict.items():
        new_dict[value] = key
    return new_dict

# print(reverse_dict(d))

# 답안
def flipped_dict(a_dict):
    return {value: key for key, value in a_dict.items()}

# print(flipped_dict(d))