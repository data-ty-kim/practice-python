# EXERCISE 18
# 마지막 줄 추출하기

# # 4장 복습 1 (14~15절)
# # ex-14
# MENU = {'sandwich' : 10, 'tea' : 7, 'salad' : 9}
# def restaurant():
#     total = 0
#     while True:
#         order = input('Order: ').strip()
#         if not order:
#             break
#         if order in MENU:
#             price = MENU[order]
#             total += price
#             print(f'{order} costs {MENU[order]}, total is {total}')
#         else:
#             print(f'Sorry, we are fresh out of {order}')

#     print(f'Your total is {total}')
        
# restaurant()


# # ex-15
# def get_rainfall():
#     rainfall = {}
#     while True:
#         city_name = input('Enter the city name: ')
#         if not city_name:
#             break
#         mm_rain = input('Enter mm rain: ')
#         rainfall[city_name] = rainfall.get(city_name, 0) + int(mm_rain)
    
#     for city, rain in rainfall.items():
#         print(f'{city}: {rain}')

# get_rainfall()


def get_final_line(file_directory):
    final_line = ''
    with open(file_directory, 'r', encoding = 'UTF8') as f:
        for current_line in f:
            final_line = current_line
        return final_line

print(get_final_line('C:/Users/user/Documents/New_PC.txt'), end = '')



# with open('C:/Users/user/Documents/New_PC.txt', 'r', encoding = 'UTF8') as f:
#     for one_line in f:
#         print(len(one_line))


# with open('C:/Users/user/Pictures/A3EBB494%942.jpg', 'rb') as f:
#     while True:
#         one_chunk = f.read(1000)
#         print(f'This chunk contains {len(one_chunk)} bytes')
#         if not one_chunk:
#             break

