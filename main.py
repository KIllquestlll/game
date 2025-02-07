from locations.location import *

class Main:


    def choice_locations(self,locations):

        print(f"Вы находитесь в {locations.title}")

        print("1.Уйти обратно.")
        print("2.Собрать вещи с локации.")
        print("3.Действие.")

        choice = int(input("Выберите действие: \n"))

        if choice == 1:
            self.main()


    def main(self):

        print("Добро пожайловать в игру!")

        print("1.Локации.")
        print("2.Функции.")

        choice = int(input("Действие: "))

        if choice == 1:
            desert = Locations("Desert",2)
            print(desert)
            print(self.choice_locations(desert))



if __name__ == '__main__':
    game = Main()
    game.main()