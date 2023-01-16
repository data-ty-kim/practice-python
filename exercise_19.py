# EXERCISE 19
# /etc/passwd를 딕셔너리로 바꾸기

# # 4장 복습 1 (16~17절)
# ex-16
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'c': 4}

# # 내 풀이
# def dictdiff(first, second):
#     union = set()
#     difference = []
#     union = first.keys() | second.keys()
#     for i in union:
#         if first[i] != second[i]:
#             difference.append((i, [first[i], second[i]]))
#     return difference

# 답안
def dictdiff(first, second):
    output = {}
    all_keys = first.keys() | second.keys()
    for key in all_keys:
        if first.get(key) != second.get(key):
            output[key] = [first.get(key), second.get(key)]
    return output

print(dictdiff(d1, d2))

# ex-17
def how_many_different_numbers(list):
    new = set(list)
    return len(new)


# 복습

def get_final_line(filename):
    with open(filename, 'r', encoding = 'UTF8') as f:
        for line in f:
            final_line = line
    return final_line

def get_final_line(filename):
    final_line = '' # final_line이 return 되어야 하기 때문에 for문 밖에 있어야 한다.
    with open(filename, 'r', encoding = 'UTF8') as f:
        for line in f:
            final_line = line
    return final_line

# print(get_final_line('C:/Users/user/Documents/New_PC.txt'), end = '')



def passwd_to_dict(filename):
    users = {}
    with open(filename) as passwd:
        for line in passwd:
            if not line.startswith(('#', '\n')):
                user_info = line.split(':')
                users[user_info[0]] = int(user_info[2])
    return users

# print(passwd_to_dict('C:/Users/user/Downloads/passwd.txt'))