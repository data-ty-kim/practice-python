# EXERCISE 28
# 숫자 결합하기

def join_number(number):
    output = [str(i) for i in range(number)]
    return ','.join(output)


print(join_number(15))

