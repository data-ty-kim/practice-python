# 제 8장 모듈과 패키지 - 모듈

# EX 36

from decimal import Decimal

rates = {
    'Chico': Decimal('0.5'),
    'Groucho': Decimal('0.7'),
    'Harpo': Decimal('0.5'),
    'Zeppo': Decimal('0.4')
    }

class HourTooLowError(Exception): pass
class HourTooHighError(Exception): pass


def time_percentage(hour):
    return hour / Decimal('24.0')


def calculate_tax(amount, state, hour):
    if hour < 0:
        raise HourTooLowError(f'Hour of {hour} is < 0')
    if hour >= 24:
        raise HourTooHighError(f'Hour of {hour} is >= 24')
    return float(amount + (amount * rates[state] * time_percentage(hour)))


def menu(**options):
    while True:
        option_string = '/'.join(sorted(options))
        choice = input(f'Enter an option ({option_string}): ')
        if choice in options:
            return options[choice]()
        print('Not a valid option')