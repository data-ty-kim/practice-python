# EXERCISE 24
# 줄 뒤집기

# 복습
import json
import glob

def print_scores(dirname):
    scores = {}
    for filename in glob.glob(f'{dirname}/*.json'):
        scores[filename] = {}

        with open(filename) as infile:
            for result in json.load(infile):
                for subject, score in result.items():       # 키와 값 추출
                    scores[filename].setdefault(subject, [])
                    scores[filename][subject].append(score)

    for one_class in scores:
        print(one_class)
        for subject, subject_scores in scores[one_class].items():
            min_score = min(subject_scores)
            max_score = max(subject_scores)
            average_score = (sum(subject_scores) / len(subject_scores))

            print(subject)
            print(f'\tmin {min_score}')
            print(f'\tmax {max_score}')
            print(f'\taverage {average_score}')

# print_scores('C:/Users/user/Downloads')


def reverse_lines(infilename, outfilename):
    with open(infilename, encoding = 'UTF8') as infile, open(outfilename, 'w', encoding = 'UTF8') as outfile:
        for one_line in infile:
            outfile.write(f'{one_line.rstrip()[::-1]}\n') 

# reverse_lines('C:/Users/user/Documents/IP.txt', 'C:/Users/user/Documents/IP_test.txt')

# strip([chars]) : 인자로 전달된 문자를 String의 왼쪽과 오른쪽에서 제거합니다.
# lstrip([chars]) : 인자로 전달된 문자를 String의 왼쪽에서 제거합니다.
# rstrip([chars]) : 인자로 전달된 문자를 String의 오른쪽에서 제거합니다.