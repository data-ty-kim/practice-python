# EXERCISE 30
# 리스트 평탄화하기

# 복습
def sum_numbers(numbers):
    output = sum(int(number) for number in numbers.split() if number.isdigit())
    return output

# print(sum_numbers('1 3 5 a b c 8 0'))



def flatten(two_dim_list):
    output = [i 
    for j in two_dim_list
    for i in j ]
    return output

print(flatten([[1,2], [3,4]]))