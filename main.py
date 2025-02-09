from locations.location import *
from player.player import *
from items.items import *

# desert = Locations("Desert",2)
#             print(desert)
#             print(self.choice_locations(desert))


hero_player = player
food = items.items.Foods
class Main:


    def choice_locations(self,locations):

        print("1.Уйти обратно.")
        print("2.Собрать вещи с локации.")
        print("3.Действие.")
        print(f"Ваши характиристики:{hero_player}")

        choice = int(input("Выберите действие: \n"))

        if choice == 1:
            return


    def ch_loc(self):

        print("Выбор локации.")
        print("1.Пустыня.")

        choice_ch = int(input("Выбор: "))
        if choice_ch == 1:

            hero_player.down_energy(3)
            hero_player.down_hungry(1)
            desert = Locations("Desert",2)

            print(desert)
            print(self.choice_locations(desert))


    def functions(self):
        while True:
            print("Ваш Функционал.")
            print("1.Сон.(Восстанавливает 5 единиц энергии)")
            print("2.Поесть.")
            print("3.Выйти.\n")
            print(f"Ваши характиристики:{hero_player}")

            choice_fun = int(input("Выбор:"))
            if choice_fun == 1:
                hero_player.up_energy(5)
                return
            elif choice_fun == 2:
                self.eating()
            elif choice_fun == 3:
                return



    def eating(self):

        print("Список еды который у вас есть!")
        print("1.Хлеб")
        print(f"Ваши характиристики:{hero_player}")

        choice_food = int(input("Выбор"))

        if choice_food == 1:
            hero_player.up_hungry(2)


    def main(self):
        while True:

            print("Добро пожайловать в игру!")

            print("1.Локации.")
            print("2.Функции.")
            print("3.Выйти.")
            print(f"Ваши характиристики:{hero_player}")
            
            try:
                choice_main = int(input("Действие: "))
            except ValueError:
                print("Можно использовать только цифры!")
                continue

            if choice_main == 1:
                self.ch_loc()
            elif choice_main == 2:
                self.functions()
            elif choice_main == 3:
                break


if __name__ == '__main__':
    game = Main()
    game.main()