
class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def añade_animal(self,animal):
        self.animals.append(animal)
        
    
    def print_all_info(self):
        print("-"*30, self.name.upper(), "-"*30)
        for animal in self.animals:
            animal.info()
    
    def todos_comen(self):
        print("-"*30, self.name.upper(), "-"*30)
        for animal in self.animals:
            animal.comer()