# EXERCISE 27
# 비밀번호 생성기 만들기

# 복습
# import operator

# def calc(to_solve):
#     operations = {'+' : operator.add,
#                  '-' : operator.sub,
#                  '*' : operator.mul,
#                  '/' : operator.truediv,
#                  '**' : operator.pow,
#                  '%' : operator.mod}

#     op, first_s, second_s = to_solve.split()
#     first = int(first_s)
#     second = int(second_s)

#     return operations[op](first, second)

# print(calc('+ 2 3'))


import random

def create_password_generator(characters):
    def create_password(length):
        output = []
        for i in range(length):
            output.append(random.choice(characters))
        return ''.join(output)
    return create_password

alpha_password = create_password_generator('abcdef')
symbol_password = create_password_generator('!@#$%')

# print(alpha_password(5))
# print(alpha_password(10))
# print(symbol_password(5))
# print(symbol_password(10))