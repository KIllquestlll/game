from locations.location import *

# desert = Locations("Desert",2)
#             print(desert)
#             print(self.choice_locations(desert))
class Main:


    def choice_locations(self,locations):

        print("1.Уйти обратно.")
        print("2.Собрать вещи с локации.")
        print("3.Действие.")

        choice = int(input("Выберите действие: \n"))

        if choice == 1:
            self.main()


    def ch_loc(self):

        print("Выбор локации.")
        print("1.Пустны.")

        choice_ch = int(input("Выбор: ","\n"))
        if choice_ch == 1:
            desert = Locations("Desert",2)
            print(desert)
            print(self.choice_locations(desert))
        


    def main(self):

        print("Добро пожайловать в игру!")

        print("1.Локации.")
        print("2.Функции.")

        choice = int(input("Действие: "))

        if choice == 1:
            self.ch_loc()


if __name__ == '__main__':
    game = Main()
    game.main()