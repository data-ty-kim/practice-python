# EXERCISE 17
# 서로 다른 숫자의 개수 찾기

# # 복습
# d1 = {'a':1, 'b':2, 'c':3}
# d2 = {'a':1, 'b':2, 'c':4}

# def dictdiff(first, second):
#     output = {}
#     union = first.keys() | second.keys()

#     for key in union:
#         if first.get(key) != second.get(key):
#             output[key] = [first.get(key), second.get(key)]
#     return output

# print(dictdiff(d1, d2))

# # 풀이도전
numbers = [1, 2, 3, 1, 2, 3, 4, 1]

# def how_many_different_numbers(list):
#     output = {}
#     for i in list:
#         output.get(i, 1)
#     return output

# print(how_many_different_numbers(numbers))


def how_many_different_numbers(numbers):
    unique_numbers = set(numbers)
    return len(unique_numbers)

print(how_many_different_numbers(numbers))