# EXERCISE 31
# 파일의 내용을 피그 라틴으로 번역하기

# 복습
def flatten(input_list):
    output_list = [i 
                    for j in input_list
                    for i in j]
    return output_list

# print(flatten([[1,2], [3,4]]))


def plword(word):
    if word[0] in 'aeiou':
        return word + 'way'

    return word[1:] + word[0] +'ay'

def plfile(filename):
    return ' '.join(plword(one_word)
                    for one_line in open(filename)
                    for one_word in one_line.split())


