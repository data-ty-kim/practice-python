# 제 10장 이터레이터와 제너레이터

# LoudIterator Class

class LoudIterator():
    def __init__(self, data):
        print('\tNow in __init__')
        self.data = data
        self.index = 0

    def __iter__(self):
        print('\tNow in __iter__')
        return self
    
    def __next__(self):
        print('\tNow in __next__')
        if self.index >= len(self.data):
            print(f'\tself.index ({self.index}) is too big; exiting')
            raise StopIteration
    
        value = self.data[self.index]
        self.index += 1
        print(f'\tGot value {value}, incremented index to {self.index}')
        return value

for one_item in LoudIterator('abc'):
    print(one_item)


def foo():
    yield 1
    yield 2
    yield 3

g=foo()
for one_item in g:
    print(one_item)


class MyEnumerate():
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = (self.index, self.data[self.index])
        self.index += 1
        return value

for index, letter in MyEnumerate('abc'):
    print(f'{index} : {letter}')


class CircleIterator():
    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times
        self.index = 0
    
    def __next__(self):
        if self.index >= self.max_times:
            raise StopIteration
        value = self.data[self.index % len(self.data)]
        self.index +=1
        return value
    
class Circle():
    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times

    def __iter__(self):
        return CircleIterator(self.data, self.max_times)

    
c = Circle('abc', 7)
print(list(c))

# EX 48

import os

def all_lines(path):
    for filename in os.listdir(path):
        full_filename = os.path.join(path, filename)
        try:
            for line in open(full_filename):
                yield line
        except OSError:
            pass
    
# EX 49
import time

def elapsed_since(data):
    last_time = None
    for item in data:
        current_time = time.perf_counter()
        delta = current_time - (last_time or current_time)
        last_time = time.perf_counter()
        yield (delta, item)

for t in elapsed_since('abcd'):
    print(t)
    time.sleep(2)


# EX 50
from itertools import chain

for one_item in chain('abc', [1,2,3], {'a': 1, 'b': 2}):
    print(one_item)



def mychain(*args):     # args는 이터러블들로 구성된 튜플
    for arg in args:
        for item in arg:
            yield item
    
for one_item in mychain('abc', [1,2,3], {'a':1, 'b':2}):
    print(one_item)