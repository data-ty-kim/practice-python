# EXERCISE 47
# 순환하는 이터레이터 만들기

# 풀이1
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


# # 풀이2 - 제너레이터
# class Circle():

#     def __init__(self, data, max_times):
#         self.data = data
#         self.max_times = max_times

#     def __iter__(self):
#         n = len(self.data)
#         return (self.data[x % n] for x in range(self.max_times))


c = Circle([1,2,3,4,5,6], 7)
print(list(c))
