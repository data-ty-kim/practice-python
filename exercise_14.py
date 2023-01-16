# EXERCISE 14
# 식당 주문 프로그램 만들기

# # 복습
# PEOPLE = [('Donald', 'Trump', 7.85),
#         ('Vladimir', 'Putin', 3.626),
#         ('Jinping', 'Xi', 10.603)]

# import operator

# def format_sort_records(list):
#     output = []
#     template = '{1:10} {0:10} {2:5.2f}'
#     for person in sorted(list, key = operator.itemgetter(1, 0)):
#         output.append(template.format(*person))
#     return output

# print('\n'.join(format_sort_records(PEOPLE))

MENU = {'sandwich': 10, 'tea': 7, 'salad': 9}

def restaurant():
    total = 0
    while True:
        order = input('Order: ').strip()
        if not order:
            break
        if order in MENU:
            price = MENU[order]
            total += price
            print(f'{order} is {price}, total is {total}')
        else:
            print(f'We are fresh out of {order} today')
        
    print(f'Your total is {total}')

restaurant()