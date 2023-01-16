# 제 7장 함수형 프로그래밍

# EX 28
def join_numbers(number):
    return ','.join([str(i) for i in range(number)])

# print(join_numbers(15))


# EX 29
def sum_numbers(numbers):
    return sum(int(number)
                for number in numbers.split()
                if number.isdigit())    


# EX 30
def flatten(input_list):
    return [i for j in input_list for i in j]

# print(flatten([[1,2], [3,4]]))


# EX 31
def plword(word):
    if word[0] in 'aeiou':
        return word + 'way'
    return word[1:] + word[0] + 'ay'

def plfile(filename):
    return ' '.join(plword(one_word) 
                    for one_line in open(filename)
                    for one_word in one_line.split())


# EX 32
d = {'a' : 1, 'b' : 2, 'c' : 3}

def flipped_dict(a_dict):
    return {key : value for value, key in a_dict.items()}


# EX 33
def transform_values(func, a_dict):
    return {key : func(value) for key, value in a_dict.items()}


# EX 34
def get_sv_1(filename):
    output_set = set()
    with open(filename, 'r') as f:
        for word in f:
            if {'a', 'e', 'i', 'o', 'u'} < {i for i in word.lower()}:
                output_set.add(word.strip())
    return output_set

def get_sv_2(filename):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return {word.strip() for word in open(filename) if vowels < set(word.lower())}

# print(get_sv('C:/Users/user/Documents/words.txt'))

# EX 35
def gema_dict():
    return {key : value for value, key in enumerate('abcdefghijklmnopqrstuvwxyz',1)}

aa_dict = gema_dict()

gema = gema_dict()

def gematria_for(word):
    return sum(gema.get(i, 0) for i in word)

# print(gematria_for('cat'))

def gematria_equal_words(word):
    gema_value = gematria_for(word.lower())
    return [i.strip() 
            for i in open('C:/Users/user/Documents/words.txt')
            if gematria_for(i.lower()) == gema_value]

print(gematria_equal_words('cat'))