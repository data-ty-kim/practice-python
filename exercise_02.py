# EXERCISE 02.
# 숫자 더하기

# # 복습. 잘 돌아가는군.
# import random

# def guessing_game():
#     answer = random.randint(0,100)
#     while True:
#         number = int(input('Enter your number: '))
#         if number > answer:
#             print('Smaller')
#         elif number < answer:
#             print('Bigger')
#         else:
#              print('Correct!')
#              break

# guessing_game()

# # 풀이 도전
# def mysum(*numbers):
#     .__init__()

def mysum(*numbers):
    output = 0
    for number in numbers:
        output += number
    return output

print(mysum(1,2,3,4))
