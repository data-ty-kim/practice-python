# EXERCISE 37
# 함수 호출은 사용자에게 맡기기

# 복습
from decimal import Decimal 

FREEDONIA = {'Chico' : Decimal('0.5'),
             'Groucho' : Decimal('0.7'),
             'Harpo' : Decimal('0.5'),
             'Zeppo' : Decimal('0.4')}

class HourTooLowError(Exception): pass
class HourTooHighError(Exception) : pass

def calculate_tax(price, place, time):
    if time < 0:
        raise HourTooLowError(f'Error: {time} is < 0')
    if time >= 24:
        raise HourTooHighError(f'Error: {time} is >= 24')
    
    return float(price + price*FREEDONIA[place]*(time/Decimal('24.0')))


# print(calculate_tax(500, 'Harpo', 12))


from menu import menu

def func_a():
    return "A"

def func_b():
    return "B"

return_value = menu(a=func_a, b=func_b)
print(f'Result is {return_value}')