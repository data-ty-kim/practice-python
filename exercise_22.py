# EXERCISE 22
# CSV 읽고 쓰기

# 복습
# import os

# def find_longest_word(filename):
#     longest_word = ''
#     with open(filename) as f:
#         for one_line in f:
#             for one_word in one_line.split():
#                 if len(one_word) > len(longest_word):
#                     longest_word = one_word
#     return longest_word

# def find_all_longest_words(dirname):
#     return {
#         filename:
#             find_longest_word(os.path.join(dirname, filename))
#             for filename in os.listdir(dirname)
#             if os.path.isfile(os.path.join(dirname, filename))
#     }

import csv

def passwd_to_csv(passwd_filename, csv_filename):
    with open(passwd_filename) as passwd, open(csv_filename, 'w') as output:
        infile = csv.reader(passwd, delimiter = ':')    # ':' 로 구분하여 리스트로 리턴
        outfile = csv.writer(output, delimiter = '\t')
        for record in infile:
            if len(record) > 1:
                outfile.writerow((record[0], record[2]))

passwd_to_csv('C:/Users/user/Downloads/passwd.txt', 'C:/Users/user/Documents/output.csv')