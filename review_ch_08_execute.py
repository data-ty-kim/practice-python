# 제 8장 모듈과 패키지 - 실행

# EX 36

from review_ch_08_module import calculate_tax, menu

tax_at_12noon = calculate_tax(100, 'Harpo', 12)

print()
print(f'You owe a total of: {tax_at_12noon}')
print()


def func_a():
    return "A"


def func_b():
    return "B"


return_value = menu(a=func_a, b=func_b)
print(f'Result is {return_value}')