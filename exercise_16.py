# EXERCISE 16
# 두 딕셔너리의 차이 찾기

# 복습
def get_rainfall():
    output = {}
    while True:
        city_name = input('name of city: ')
        if not city_name:
            break
        mm_rain = input('Enter mm rain: ')
        if not mm_rain:
            mm_rain = 0
        output[city_name] = output.get(city_name, 0) + int(mm_rain)
    
    for city, rain in output.items():
        print(f'{city}: {rain}')

get_rainfall()


# 풀이도전
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'c': 4}

def dictdiff(first, second):
    output = {}
    all_keys = first.keys() | second.keys()     # | 합집합연산
    for key in all_keys:
        if first.get(key) != second.get(key):
            output[key] = [first.get(key), second.get(key)]
    return output



