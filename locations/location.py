class Locations:

    def __init__(self,title,distance):
        self.title = title
        self.distance = distance

    def __str__(self):
        return f"Добро пожайловать в {self.title}"


    def Desert(self):
        
        Desert_location = Locations("Desert",2)
        return Desert_location
