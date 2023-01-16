# EXERCISE 10
# 아무것이나 더하기

# # 복습
# def firstlast(seq):
#     return seq[:1] + seq[-1:]

# print(firstlast('apple'))
# print(firstlast([1,2,3,4]))

# # 풀이 도전
# def mysum(*args):
#     return 

def mysum(*items):
    if not items:
        return items
    
    output = items[0]
    for item in items[1:]:
        output += item
    
    return output

print(mysum())
print(mysum(10,20,30,40))
print(mysum('a','b','c','d'))
print(mysum([10,20,30], [40,50,60], [70,80]))
