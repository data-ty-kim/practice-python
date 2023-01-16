# EXERCISE 33
# 값 변환하기

# 복습
d = {'a' : 1, 'b' : 2, 'c' : 3}

# def reverse_dict(input_dict):
#     return {value: key for key, value in input_dict.items()}

# print(reverse_dict(d))


def transform_values(func, dict_a):
    return {key: func(value) for key, value in dict_a.items()}

