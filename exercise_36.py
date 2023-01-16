# EXERCISE 36
# 판매세 계산하기

from decimal import Decimal

RATES = {'Chico' : Decimal('0.5'), 
         'Groucho' : Decimal('0.7'), 
         'Harpo' : Decimal('0.5'), 
         'Zeppo' : Decimal('0.4')}

class HourTooLowError(Exception): pass
class HourTooHighError(Exception) : pass


def time_percentage(hour):
    return hour / Decimal('24.0')


def calculate_tax(amount, state, hour):
    if hour < 0:
        raise HourTooLowError(f'Hour of {hour} is < 0')
    if hour >= 24:
        raise HourTooHighError(f'Hour of {hour} is >=24')

    return float(amount + 
                 (amount * RATES[state] * time_percentage(hour)))



