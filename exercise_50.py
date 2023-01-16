# EXERCISE 50
# mychain 함수 만들기

def mychain(*args):
    for arg in args:
        for item in arg:
            yield item

for one_item in mychain('abc', [1,2,3], {'a':1, 'b':2}):
    print(one_item)