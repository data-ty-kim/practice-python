# EXERCISE 38
# 아이스크림 스쿱 만들기

class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor
    
def create_scoop():
    scoops = [Scoop('chocolate'),
              Scoop('vanilla'),
              Scoop('persimmon')]
    for scoop in scoops:
        print(scoop.flavor)

create_scoop()

