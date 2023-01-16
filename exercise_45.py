# EXERCISE 45
# 동물원 만들기

from exercise_44 import *

class Zoo():
    def __init__(self):
        self.cages = []
    
    def add_cages(self, *cages):
        for one_cage in cages:
            self.cages.append(one_cage)
    
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

wolf = Wolf('black')
sheep = Sheep('white')
snake = Snake('brown')
parrot = Parrot('green')

print()
print(wolf)
print(sheep)
print(snake)
print(parrot)
print()

c1 = Cage(1)
c1.add_animals(wolf, sheep)

c2 = Cage(2)
c2.add_animals(snake, parrot)

z = Zoo()
z.add_cages(c1, c2)

print(z)
print()
print(z.animals_by_color('white'))
print(z.animals_by_legs(4))
print(z.number_of_legs())
