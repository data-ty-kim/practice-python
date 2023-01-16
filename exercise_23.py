# EXERCISE 23
# JSON 파일 읽어 들여 처리하기

# # 복습
# import csv

# def passwd_to_csv(passwd_filename, csv_filename):
#     with open(passwd_filename) as passwd, open(csv_filename, 'w') as output:
#         infile = csv.reader(passwd, delimiter=':')
#         outfile = csv.writer(output, delimiter='\t')
#         for record in infile:
#             if len(record) > 1:
#                 outfile.writerow((record[0], record[2]))

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

# print_scores('C:/Users/user/Downloads/scores')    # json 파일이 잘못돼서 안 됨

