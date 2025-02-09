import items.items
from locations.location import *
from items.items import *


food = items.items.Foods
class Player_const:

    def __init__(self,health,hunger,energy,biom):

        self.health = health
        self.hunger = hunger
        self.energy = energy



    def __str__(self):
        return f"Здоровье:{self.health}. Голод: {self.hunger}. Энергия:{self.energy}"


    def down_energy(self,amount):
        self.energy -= amount
        if self.energy < 0:
            raise SystemExit("Вы проиграли!")


    def up_energy(self,amount):
        self.energy += amount
        if self.energy > 10:
            self.energy = 10
            print("Ваш запас энергии:10")


    def down_hungry(self,hugry):
        self.hunger -= hugry
        if self.hunger < 0:
            raise SystemExit("Вы умерли от голода!")

    def up_hungry(self,hungry):
        self.hunger += hungry
        if self.hunger > 10:
            self.hunger = 10
            print("Вы полностью сыты!")

player = Player_const(10,2,10,Locations)
    
