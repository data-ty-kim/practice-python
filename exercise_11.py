# EXERCISE 11
# 이름을 알파벳 순서로 정렬하기

# # 복습
# def mysum(*args):
#     if not args:
#         return args
#     else:
#         output = args[0]
#         for arg in args[1:]:
#             output += arg
    
#     return output

# print(mysum('abc', 'def'))
# print(mysum([1,2,3], [4,5,6]))
# print(mysum(1,2,3))


from operator import itemgetter


PEOPLE = [{
    'first' : 'Reuven', 'last' : 'Lerner',
    'email' : 'reuven@lerner.co.il'
}, {
    'first' : 'Donald', 'last' : 'Trump',
    'email' : 'president@whitehouse.gov'
}, {
    'first' : 'Vladimir', 'last' : 'Putin',
    'email' : 'president@kremvax.ru'
}]

# # 풀이 1
import operator

# def alphabetize_names(list_of_dicts):
#     return sorted(list_of_dicts, key = operator.itemgetter('last', 'first'))

# print(alphabetize_names(PEOPLE))

# # 풀이 2
# def alphabetize_names(list_of_dicts):
#     for person in sorted(list_of_dicts, key = lambda x : [x['last'], x['first']]):
#         print(f'{person["last"]}, {person["first"]}: {person["email"]}')

# alphabetize_names(PEOPLE)

print(operator.itemgetter('last', 'first'))