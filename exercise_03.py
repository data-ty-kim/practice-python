# EXERCISE 03
# 달린 시간 계산하기

# 복습

#  def mysum(*numbers):
#     output = 0
#     for number in numbers:
#         output += number
#     return output

# # 풀이 도전

# def run_timing(*runtime):
#     average = 0
#     run = float(input('Enter 10 km run time: '))
#     for run in runtime:
#         average += run

#     print('Average of {}, over {} runs'.format(average/len(runtime), len(runtime)))

# run_timing()

def run_timing():
    number_of_runs = 0
    total_time = 0

    while True:
        one_run = input('Enter 10 km run time: ')

        if not one_run:
            break

        number_of_runs += 1
        total_time += float(one_run)

    average_time = total_time / number_of_runs

    print('Average of {:.2f}, over {} runs'.format(average_time, number_of_runs))

run_timing()