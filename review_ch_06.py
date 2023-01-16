# 제 6장 함수

# EX 25
def myxml(tagname, content = '', **kwargs):
    attrs = ''.join([f' {key}="{value}"'
                    for key, value in kwargs.items()])
    return f'<{tagname}{attrs}>{content}</{tagname}>'

print(myxml('tagname', 'hello', a=1, b=2, c=3))


# EX 26
import operator

def calc(to_solve):
    operations = {'+' : operator.add,
                  '-' : operator.sub,
                  '*' : operator.mul,
                  '/' : operator.truediv,
                  '**' : operator.pow,
                  '%' : operator.mod}

    op, first_s, second_s = to_solve.split()
    first = int(first_s)
    second = int(second_s)

    return operations[op](first, second)

# EX 27
import random

def create_password_generator(characters):
    def create_password(length):
        output = []
        for i in range(length):
            output.append(random.choice(characters))
        return ''.join(output)
    return create_password

    

