# 제 5장 파일

# EX 18
def get_final_line(filename):
    final_line = ''
    with open(filename, 'r', encoding='UTF8') as f:
        for line in f:
            final_line = line
    return final_line

# print(get_final_line('C:/Users/user/Documents/New_PC.txt'))

# EX 19
def passwd_to_dict(filename):
    dict = {}
    with open(filename, 'r', encoding='UTF8') as f:
        for line in f:
            list = line.split(':')
            if len(list) > 2:            # 답안은 if not line.startswith(('#','\n')):으로 처리
                dict[list[0]] = list[2]
    return dict

# print(passwd_to_dict('C:/Users/user/Downloads/passwd.txt'))

# EX 20
def wordcount(filename):
    dict_0 = {'글자 수' : 0, '단어 수' : 0, '줄 수' : 0, '유일한 단어 수' : 0}
    set_0 = set()
    with open(filename, 'r', encoding='UTF8') as f:
        for line in f:
            dict_0['글자 수'] += len(line) - 1
            dict_0['단어 수'] += len(line.split())
            dict_0['줄 수'] += 1
            set_0.update(line.split())
        dict_0['유일한 단어 수'] = len(set_0)
    for i, j in dict_0.items():
        print(f'{i}:{j}')

# wordcount('C:/Users/user/Documents/New_PC.txt')

# EX 21
def find_longest_word(filename):
    longest_word = ''
    with open(filename, encoding='UTF8') as f:
        for line in f:
            for word in line.split():
                if len(word) > len(longest_word):
                    longest_word = word
    return longest_word

# print(find_longest_word('C:/Users/user/Documents/New_PC.txt'))

import os
from re import sub
from tabnanny import filename_only

from numpy import maximum_sctype

def find_all_longest_words(dirname):
    return {
        filename: find_longest_word(os.path.join(dirname, filename))
        for filename in os.listdir(dirname)
        if os.path.isfile(os.path.join(dirname, filename))  # 폴더 말고 파일만 읽기 위해서
    }

# EX 22
import csv

def passwd_to_csv(passwd_filename, csv_filename):
    with open(passwd_filename) as passwd, open(csv_filename, 'w') as output:
        infile = csv.reader(passwd, delimiter=':')
        outfile = csv.writer(output, delimiter='\t')
        for record in infile:
            if len(record) > 1:
                outfile.writerow((record[0], record[2]))

# passwd_to_csv('C:/Users/user/Downloads/passwd.txt', 'C:/Users/user/Downloads/passwd.csv')

# EX 23
import json
import glob

def print_scores(dirname):
    scores = {}
    for filename in glob.glob(f'{dirname}/*.json'):
        scores[filename] = {}
        with open(filename) as infile:
            for result in json.load(infile):
                for subject, score in result.items():
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

# EX 24 - 다시 해보기.
def reverse_line(infilename, outfilename):
    with open(infilename, 'r', encoding='UTF8') as f_i, open(outfilename, 'w') as f_o:
        for line in f_i:
            f_o.write(f'{line.rstrip()[::-1]}\n')