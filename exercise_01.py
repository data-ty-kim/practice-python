# EXERCISE 01.
# 숫자 맞히기 게임

import random

# 내가 풀이하다 망한 거.
# def guessing_game():
#     number = random.randimt(0, 101)
#     name = input('Enter your name: ')
#     print(f'Hello, {name}!')
#     if number > 70:
#         print('Too High')
#     elif number >30:
#         print('Too Low')
#     else:
#         print('Just Right')

def guessing_game():
    answer = random.randint(0, 100)

    while True:
        user_guess = int(input('What is your guess?'))
        if user_guess == answer:
            print(f'Right! The answer is {user_guess}')
            break
        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low')
        else:
            print(f'Your guess of {user_guess} is too high!')

guessing_game()