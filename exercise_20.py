# EXERCISE 20
# 글자 수 세기

# 복습
# def passwd_to_dict(file):
#     dict = {}
#     with open(file) as f:
#         for line in f:
#             temp = line.split(':')
#             dict[temp[0]] = int(temp[2])
#     return dict
# 작동 안 하네 ㅠㅠ

# def passwd_to_dict(file):
#     dict = {}
#     with open(file) as f:
#         for line in f:
#             if not line.startswith(('#', '\n')):
#                 temp = line.split(':')
#                 dict[temp[0]] = int(temp[2])
#     return dict

# print(passwd_to_dict('C:/Users/user/Downloads/passwd.txt'))

# 풀이도전
# def wc(file):
#     total = 0
#     total_words = []
#     sep_words = []
#     with open(file, 'r', encoding = 'UTF8') as f:
#         for line in f:
#             total_words.append(line)
#             sep_words.append(line.split())
#     unique_words = set(sep_words)
#     for i in total_words:
#         total += sum(len(i))

#     print('글자 수: {}\n단어 수: {}\n줄 수: {}\n유일한 단어 수: {}'.format(
#             total, len(sep_words), len(total_words), len(unique_words)
#     ))

# wc('C:/Users/user/Documents/New_PC.txt')

def wordcount(filename):
    counts = {'characters': 0, 'words' : 0, 'lines' : 0}
    unique_words = set()

    for one_line in open(filename, 'r', encoding = 'UTF8'):
        counts['lines'] += 1
        counts['characters'] += len(one_line)
        counts['words'] += len(one_line.split())
        unique_words.update(one_line.split())
    counts['unique words'] = len(unique_words)
    for key, value in counts.items():
        print(f'{key:<12}:{value:>5}')

wordcount('C:/Users/user/Documents/New_PC.txt')