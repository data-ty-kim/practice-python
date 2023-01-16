# 제 9장 객체 
# 아이스크림 예제

class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl():
    max_scoops = 3

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for one_scoop in new_scoops:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(one_scoop)
    
    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)

class BigBowl(Bowl):
    max_scoops = 5

s1 = Scoop('chocolate')
bb = BigBowl()
bb.add_scoops(s1)
# print(bb)


# dict를 상속해서 FlexibleDict 클래스 만들기

class FlexibleDict(dict):
    def __getitem__(self, key):
        try:
            if key in self:
                pass
            elif str(key) in self:
                key = str(key)
            elif int(key) in self:
                key = int(key)
        except ValueError:
            pass

        return dict.__getitem__(self, key)


# 동물원 예제

class Animal():
    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs
    
    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'
    
class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)        

class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)

class Cage():
    def __init__(self, id_number):
        self.id_number = id_number
        self.animals = []
    
    def add_animals(self, *animals):
        for one_animal in animals:
            self.animals.append(one_animal)
    
    def __repr__(self):
        output = f'Cage {self.id_number}\n'
        output += '\n'.join(
            '\t' + str(animal) for animal in self.animals)
        return output

wolf = Wolf('black')
sheep = Sheep('white')
snake = Snake('brown')
parrot = Parrot('green')

c1 = Cage(1)
c1.add_animals(wolf, sheep)

c2 = Cage(2)
c2.add_animals(snake, parrot)


class Zoo():
    def __init__(self):
        self.cages = []
    
    def add_cages(self, *cages):
        self.cages.extend(cages)

    def __repr__(self):
        return '\n'.join(str(one_cage)
            for one_cage in self.cages)
    
    def animals_by_color(self, color):
        return [one_animal
            for one_cage in self.cages
            for one_animal in one_cage.animals
            if one_animal.color == color]
    
    def animals_by_legs(self, number_of_legs):
        return [one_animal
            for one_cage in self.cages
            for one_animal in one_cage.animals
            if one_animal.number_of_legs == number_of_legs]

    def number_of_legs(self):
        return sum(one_animal.number_of_legs
            for one_cage in self.cages
            for one_animal in one_cage.animals)

z = Zoo()
z.add_cages(c1, c2)

print()
print(z)
print(z.animals_by_color('white'))
print(z.animals_by_legs(4))
print(z.number_of_legs())
