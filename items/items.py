class Item:
    def __init__(self,title,amount):

        self.title = title
        self.amount = amount


    def __str__(self):
        return f"Предмет:{self.title} его значимость:{self.amount}"



class Foods:

    def __init__(self,title,amount):

        self.title = title
        self.amount = amount

    def __str__(self):
        return f"Еда: {self.title} Сытость: {self.amount}"

    def Bread(self):
        Bread_Food = Foods("Хлеб",3)

