# EXERCISE 15
# 강수량 계산하기

# # 복습
# MENU = {'sandwich': 10, 'tea': 7, 'salad': 9}

# def restaurant():
#     total = 0
#     while True:
#         order = input('Order: ').strip()

#         if not order:
#             break
#         if order in MENU:
#             value = MENU[order]
#             total += value
#             print(f'{order} is {value} , total is {total}')
#         else:
#             print(f'Sorry, we are fresh out of {order} today.')

#     print(f'Your total is {total}')

# restaurant()

# # 풀이도전
# CITY = {'Boston': 5, 'New York': 7}

# def get_rainfall():
#     output = []
#     while True:
#         city = input('city name?: ').strip()
#         if city in CITY:
#             output.append(CITY[city])
#         if not city:
#             break
#     return output
#     print(''.join(output))

# get_rainfall()

def get_rainfall():
    rainfall = {}

    while True:
        city_name = input('Enter city name: ')
        if not city_name:
            break

        mm_rain = input('Enter mm rain: ')
        rainfall[city_name] = rainfall.get(city_name, 0) + int(mm_rain)

    for city, rain in rainfall.items():
        print(f'{city}: {rain}')

get_rainfall()



