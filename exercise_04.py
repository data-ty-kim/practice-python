# EXERCISE 04
# 16진수 출력하기

# 복습1
# def run_timing():
#     run_time = 0
#     runs = 0
#     while True:
#         one_run = input('Enter 10 km run time: ')
#         if not one_run:
#             break
#         run_time += float(one_run)
#         runs += 1

#     print('Average of {}, over {} runs'.format(run_time/runs, runs))

# run_timing()

# 아아, 공백을 while 문 안에 float(input('sentence'))로 받으니까 에러난다.

# 풀이 도전
# def hex_output():
#     print((hex(int(input('number: ')))))

# hex_output()

def hex_output():
    decnum = 0
    hexnum = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hexnum)):
        decnum += int(digit, 16) * (16 ** power)
    print(decnum)

hex_output()

